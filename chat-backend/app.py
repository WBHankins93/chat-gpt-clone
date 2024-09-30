# /backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

# OpenAI API Key Configuration
openai.api_key = "OPENAI_API_KEY"

# Route to Handle Chat Requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    # Generate AI response using OpenAI API (this can be mocked for testing)
    response = openai.Completion.create(
        model="text-davinci-003",  # Use appropriate GPT model
        prompt=user_message,
        max_tokens=100
    )
    ai_response = response.choices[0].text.strip()

    # Send response back to frontend
    return jsonify({"response": ai_response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
