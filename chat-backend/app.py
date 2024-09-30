# /backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os
import uuid  # For generating conversation_id
from models import db, Chat  # Import db and Chat model

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "http://localhost:3000"}})

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# OpenAI API Key Configuration
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Server is running!"

# Route to Handle Chat Requests
@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    data = request.json
    user_message = data.get('message')
    conversation_id = data.get('conversation_id') or str(uuid.uuid4())
    
    # Generate AI response using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ],
        max_tokens=100
    )
    ai_response = response.choices[0].message['content'].strip()


    # Save chat to the database
    chat_entry = Chat(conversation_id=conversation_id, user_message=user_message, ai_response=ai_response)
    db.session.add(chat_entry)
    db.session.commit()

    return jsonify({"response": ai_response, "conversation_id": conversation_id})


@app.route('/chats/<conversation_id>', methods=['GET'])
def get_chats(conversation_id):
    # Query all chats with the specified conversation_id
    chats = Chat.query.filter_by(conversation_id=conversation_id).all()
    chat_history = [
        {"user_message": chat.user_message, "ai_response": chat.ai_response, "timestamp": chat.timestamp}
        for chat in chats
    ]

    return jsonify(chat_history)

# Run the Flask app
if __name__ == '__main__':
    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()  # This will create chats.db and the required table schema
    app.run(debug=True)
