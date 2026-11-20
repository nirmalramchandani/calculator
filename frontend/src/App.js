import React, { useState } from 'react';
import './App.css'; // For component-specific styles
import axios from 'axios';

function App() {
    const [name, setName] = useState('');
    const [selectedEmojis, setSelectedEmojis] = useState('');
    const [stickerUrl, setStickerUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

    const handleGenerateSticker = async () => {
        setError('');
        setStickerUrl('');
        setLoading(true);
        try {
            const response = await axios.post(`${API_URL}/generate-sticker`, {
                name,
                emojis: selectedEmojis
            });
            setStickerUrl(response.data.sticker);
        } catch (err) {
            console.error('Error generating sticker:', err);
            setError('Failed to generate sticker. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const emojiOptions = ['😀', '👍', '❤️', '🚀', '🌟', '🎉', '💡', '🔥', '💻', '✨'];

    return (
        <div className="App">
            <header className="App-header">
                <h1>Sticker Creator</h1>
                <p>Enter your name, choose some emojis, and get a custom sticker!</p>
            </header>

            <div className="sticker-form">
                <div className="input-group">
                    <label htmlFor="name-input">Your Name:</label>
                    <input
                        id="name-input"
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="e.g., Jane Doe"
                        maxLength="20"
                    />
                </div>

                <div className="input-group">
                    <label>Select Emojis:</label>
                    <div className="emoji-picker">
                        {emojiOptions.map((emoji) => (
                            <button
                                key={emoji}
                                className={`emoji-button ${selectedEmojis.includes(emoji) ? 'selected' : ''}`}
                                onClick={() => {
                                    setSelectedEmojis(prev =>
                                        prev.includes(emoji)
                                            ? prev.replace(emoji, '') // Remove if already selected
                                            : (prev + emoji).slice(0, 5) // Add if not, limit total emojis
                                    );
                                }}
                            >
                                {emoji}
                            </button>
                        ))}
                    </div>
                    <input
                        type="text"
                        value={selectedEmojis}
                        onChange={(e) => setSelectedEmojis(e.target.value)}
                        placeholder="Or type your own emojis here"
                        maxLength="10"
                        className="manual-emoji-input"
                    />
                    <small>Max 5 emojis recommended for best display.</small>
                </div>

                <button onClick={handleGenerateSticker} disabled={loading || (!name && !selectedEmojis)} className="generate-button">
                    {loading ? 'Generating...' : 'Generate Sticker'}
                </button>

                {error && <p className="error-message">{error}</p>}

                {stickerUrl && (
                    <div className="sticker-output">
                        <h2>Your Sticker:</h2>
                        <img src={stickerUrl} alt="Generated Sticker" className="generated-sticker-image" />
                        <a href={stickerUrl} download="my-sticker.png" className="download-button">Download Sticker (PNG)</a>
                    </div>
                )}
            </div>

            <footer className="App-footer">
                <p>&copy; 2023 Sticker Creator. All rights reserved.</p>
            </footer>
        </div>
    );
}

export default App;
