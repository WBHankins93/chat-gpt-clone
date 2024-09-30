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
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# OpenAI API Key Configuration
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route to Handle Chat Requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    conversation_id = data.get('conversation_id') or str(uuid.uuid4())
    
    # Generate AI response using OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",  # Using this model to be cost friendly. To have a more accurate response, we can use gpt-3.5-turbo.
        prompt=user_message,
        max_tokens=100
    )
    ai_response = response.choices[0].text.strip()

    # Save chat to the database
    chat_entry = Chat(conversation_id=conversation_id, user_message=user_message, ai_response=ai_response)
    db.session.add(chat_entry)
    db.session.commit()

    return jsonify({"response": ai_response, "conversation_id": conversation_id})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
