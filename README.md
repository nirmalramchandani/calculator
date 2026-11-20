# Sticker Creator

This project is a web application that allows users to create custom stickers by entering their name and selecting emojis. The application uses a Flask backend for generating image stickers and a React frontend for the user interface.

## Features

-   Enter your name to be included in the sticker.
-   Select from a list of predefined emojis or type your own.
-   Generate a custom sticker image (PNG format).
-   Download the generated sticker.

## Technologies Used

**Backend:**
-   **Python Flask:** A lightweight web framework for the API.
-   **Pillow (PIL Fork):** For image generation and manipulation.
-   **Flask-CORS:** To handle Cross-Origin Resource Sharing for frontend/backend communication.

**Frontend:**
-   **React:** A JavaScript library for building user interfaces.
-   **Axios:** For making HTTP requests to the backend API.
-   **HTML/CSS:** For structuring and styling the web pages.

## Project Structure

```
sticker-creator/
├── backend/
│   ├── app.py              # Flask application for sticker generation
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/             # Public assets for React (e.g., index.html)
│   ├── src/                # React source code
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json        # Node.js dependencies for React app
│   └── .env                # Environment variables for frontend
└── README.md               # Project overview and setup instructions
```

## Setup and Installation

Follow these steps to set up and run the Sticker Creator application locally.

### 1. Clone the Repository (Simulated)

In a real scenario, you would clone the repository. For this exercise, assume these files are provided in your working directory.

### 2. Backend Setup

1.  Navigate into the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   **On Windows:** `.\venv\Scripts\activate`
    -   **On macOS/Linux:** `source venv/bin/activate`
4.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the Flask application:
    ```bash
    python app.py
    ```
    The backend server will start on `http://localhost:5000`.

### 3. Frontend Setup

1.  Open a new terminal and navigate into the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the Node.js dependencies:
    ```bash
    npm install
    # or if you use yarn
    # yarn install
    ```
3.  Ensure the `.env` file exists with the API URL:
    ```
    # frontend/.env
    REACT_APP_API_URL=http://localhost:5000
    ```
    This tells the React app where to find your Flask backend.
4.  Run the React development server:
    ```bash
    npm start
    # or
    # yarn start
    ```
    The frontend application will typically open in your browser at `http://localhost:3000`.

## Usage

1.  Ensure both the Flask backend and React frontend servers are running.
2.  Open your browser to the frontend address (e.g., `http://localhost:3000`).
3.  Enter your name in the input field.
4.  Select emojis using the buttons or type them directly into the input.
5.  Click the "Generate Sticker" button.
6.  Your custom sticker will appear below, with an option to download it.

## Notes on Emoji Rendering

The quality of emoji rendering on the generated sticker can depend on the fonts available on the server where the Flask application is running. For optimal emoji display, a system with comprehensive emoji font support (e.g., Noto Color Emoji) would be beneficial. In this implementation, a generic font is attempted, and emojis are rendered as text characters, which may not always appear as full-color emojis without a proper emoji font installed on the server.

## Potential Enhancements

-   Allow users to upload custom background images.
-   More advanced text formatting options (colors, fonts, sizes).
-   Drag-and-drop interface for emoji placement.
-   User accounts and sticker gallery.
-   Deployment to production environments (e.g., Heroku, AWS, Vercel).
-   Better error handling and input validation.
-   Using a dedicated emoji rendering library on the backend for consistent emoji appearance.
