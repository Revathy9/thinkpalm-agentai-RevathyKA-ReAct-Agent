import React, { useState, useEffect } from "react";
import "./App.css";
import { sendMessage, fetchMemory } from "./api";

function App() {
    const [message, setMessage] = useState("");
    const [responses, setResponses] = useState([]);
    const [loading, setLoading] = useState(false);
    const [memory, setMemory] = useState(null);

    // Fetch memory on load
    useEffect(() => {
        loadMemory();
    }, []);

    const loadMemory = async () => {
        const mem = await fetchMemory();
        if (mem && mem.last_message) {
            setMemory(mem.last_message);
        }
    };

    const handleSend = async () => {
        if (!message) return;
        setLoading(true);
        setResponses([]);
        try {
            const result = await sendMessage(message);
            setResponses(result.response || []);
            // Update memory immediately after sending
            await loadMemory();
        } catch (error) {
            console.error(error);
            alert("Backend Error - Make sure your backend server is running and Gemini API key is configured.");
        }
        setLoading(false);
    };

    return (
        <div className="app-container">
            <div className="background-glows">
                <div className="glow glow-1"></div>
                <div className="glow glow-2"></div>
            </div>

            <div className="card-container">
                <header className="app-header">
                    <div className="logo-section">
                        <div className="logo-spark">✨</div>
                        <h1>AURA</h1>
                    </div>
                    <p className="subtitle">Agentic Weather & Reminder Assistant</p>
                </header>

                {memory && (
                    <div className="memory-badge">
                        <span className="memory-icon">🧠</span>
                        <span className="memory-text">Memory: "{memory}"</span>
                    </div>
                )}

                <div className="input-group">
                    <input
                        type="text"
                        placeholder="Try: check weather and remind me to carry umbrella"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && handleSend()}
                        disabled={loading}
                    />
                    <button onClick={handleSend} disabled={loading} className={loading ? "loading" : ""}>
                        {loading ? (
                            <div className="spinner"></div>
                        ) : (
                            <>
                                <span>Send</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                    <line x1="22" y1="2" x2="11" y2="13"></line>
                                    <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                                </svg>
                            </>
                        )}
                    </button>
                </div>

                <div className="response-box">
                    {responses.length === 0 && !loading && (
                        <div className="empty-state">
                            <p>Ask AURA to check the weather in Kochi, set a reminder, or both!</p>
                            <div className="suggestions">
                                <div className="suggestion-chip" onClick={() => setMessage("check weather in Kochi")}>
                                    🌤️ Check weather
                                </div>
                                <div className="suggestion-chip" onClick={() => setMessage("remind me to carry water bottle")}>
                                    ⏰ Set a reminder
                                </div>
                                <div className="suggestion-chip" onClick={() => setMessage("check weather and remind me to buy milk")}>
                                    ⚡ Both together
                                </div>
                            </div>
                        </div>
                    )}

                    {responses.map((item, index) => {
                        const isWeather = item.toLowerCase().includes("weather") || item.toLowerCase().includes("kochi");
                        const isReminder = item.toLowerCase().includes("reminder") || item.toLowerCase().includes("remind");
                        
                        return (
                            <div key={index} className={`response-card ${isWeather ? 'weather-card' : isReminder ? 'reminder-card' : ''}`}>
                                <div className="card-header">
                                    <span className="card-icon">{isWeather ? "🌤️" : isReminder ? "🔔" : "🤖"}</span>
                                    <h3>{isWeather ? "Weather Intelligence Agent" : isReminder ? "Reminder Agent" : "Coordinator Agent"}</h3>
                                </div>
                                <div className="card-body">
                                    {item.split("\n").map((line, lIdx) => (
                                        <p key={lIdx}>{line}</p>
                                    ))}
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}

export default App;
