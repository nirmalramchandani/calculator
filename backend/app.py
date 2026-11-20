from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Try to load a suitable font. Fallback if not found.
# For emojis, a specific font like 'NotoColorEmoji.ttf' would be ideal,
# but it's not universally available. System fonts might render them.
try:
    # A common font that might be available on some systems (Windows/macOS)
    # For Linux, you might need to specify a path to a font like 'DejaVuSans.ttf' or 'NotoSans-Regular.ttf'
    # Or, if you have a custom font file in your project, e.g., 'static/font.ttf'
    # font_path = "static/font.ttf"
    font_path = "arial.ttf" # Consider using a bundled font for better cross-platform consistency
    name_font = ImageFont.truetype(font_path, 40)
    emoji_font = ImageFont.truetype(font_path, 60) # Larger for emojis
except IOError:
    # Fallback to default PIL font if specified font is not found
    name_font = ImageFont.load_default()
    emoji_font = ImageFont.load_default()
    print("Warning: Could not load specific font. Using default PIL font. Emojis might not render correctly.")


@app.route('/generate-sticker', methods=['POST'])
def generate_sticker():
    data = request.json
    name = data.get('name', 'Builder')
    emojis = data.get('emojis', '')

    if not name and not emojis:
        return jsonify({"error": "Name or emojis must be provided"}), 400

    # Sticker dimensions
    width, height = 400, 400
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0)) # Transparent background
    draw = ImageDraw.Draw(img)

    # Calculate text sizes
    # getbbox gives (left, top, right, bottom)
    name_bbox = draw.textbbox((0,0), name, font=name_font)
    name_width = name_bbox[2] - name_bbox[0]
    name_height = name_bbox[3] - name_bbox[1]

    emoji_bbox = draw.textbbox((0,0), emojis, font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_height = emoji_bbox[3] - emoji_bbox[1]

    # Positions
    name_x = (width - name_width) / 2
    name_y = (height / 2) - (name_height / 2) - (emoji_height / 2)
    emoji_x = (width - emoji_width) / 2
    emoji_y = (height / 2) + (name_height / 2) - (emoji_height / 2)

    # Draw text with a black outline for better visibility
    def draw_text_with_outline(draw_obj, xy, text, font, fill_color, outline_color=(0,0,0), outline_width=2):
        x, y = xy
        # Draw outline
        for dx, dy in [(w, h) for w in range(-outline_width, outline_width + 1) for h in range(-outline_width, outline_width + 1) if w*w + h*h <= outline_width*outline_width]:
            draw_obj.text((x + dx, y + dy), text, font=font, fill=outline_color)
        # Draw main text
        draw_obj.text(xy, text, font=font, fill=fill_color)

    draw_text_with_outline(draw, (name_x, name_y), name, name_font, (0, 0, 0)) # Black for name
    draw_text_with_outline(draw, (emoji_x, emoji_y), emojis, emoji_font, (255, 215, 0)) # Gold for emojis

    # Convert image to bytes
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')
    encoded_img = base64.b64encode(byte_arr.getvalue()).decode('ascii')

    return jsonify({'sticker': f'data:image/png;base64,{encoded_img}'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
