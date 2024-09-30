import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  // Function to handle sending messages to the Flask backend
  const sendMessage = async () => {
    if (!message.trim()) return;
  
    try {
      // Send a POST request to the Flask backend
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
  
      // Check for non-OK response
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
      
      // Update chat history with the new message and AI response
      setChatHistory([...chatHistory, { user: message, ai: data.response }]);
      setMessage(''); // Clear input field
    } catch (error) {
      console.error("Failed to send message:", error);
    }
  };
  

  return (
    <div className="app-container">
      <h1>Chat GPT Clone</h1>
      <div className="chat-box">
        {chatHistory.map((chat, index) => (
          <div key={index}>
            <strong>You:</strong> {chat.user}
            <br />
            <strong>AI:</strong> {chat.ai}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
        className="message-input"
      />
      <button onClick={sendMessage} className="send-button">
        Send
      </button>
    </div>
  );
}

export default App;
