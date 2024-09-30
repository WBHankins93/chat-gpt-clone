# ChatGPT Clone

A simple, full-stack chat application that mimics basic ChatGPT functionality. This project consists of a **Flask backend** and a **React frontend** that allows users to chat with an AI model and saves conversations in a database.

---

## **Table of Contents**
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Future Improvements](#future-improvements)

---

## **Features**

- Real-time chat interface powered by React.
- Communication between frontend and backend using RESTful APIs.
- Chat messages are saved and retrieved from a database.
- AI responses generated using OpenAI's API.

---

## **Tech Stack**

### **Backend**
- **Python**: Main language for server-side development.
- **Flask**: Web framework for the backend.
- **Flask-CORS**: Enables cross-origin requests between frontend and backend.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight database for development.

### **Frontend**
- **React**: UI library for building the chat interface.
- **CSS**: Styling for the user interface.

---

## **Setup Instructions**

### **Backend Setup**

1. **Navigate to the `chat-backend` Directory**
   ```bash
   cd chat-gpt-clone/chat-backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install Flask Flask-CORS SQLAlchemy
   ```

5. **Run the Flask Application**
   ```bash
   flask run
   ```

### **Frontend Setup**

1. **Navigate to the `chat-frontend` Directory**
   ```bash
   cd chat-gpt-clone/chat-frontend
   ```

2. **Install Node.js and npm**
   - Follow the instructions on the [Node.js website](https://nodejs.org/) to install the latest version.

3. **Install Project Dependencies**
   ```bash
   npm install
   ```

4. **Start the Development Server**
   ```bash
   npm start
   ```

---

## **Usage**

1. **Open Your Browser**
   - Navigate to `http://localhost:3000` to access the chat interface.

2. **Start Chatting**
   - Enter your message in the input field and click "Send" to see the AI response.

---

## **Important Notes**

- Ensure that the Flask backend is running before starting the frontend.
- The AI model used here is the `text-davinci-003` model, which is a basic model. For a more accurate response, you can use `gpt-3.5-turbo`.

---

## **Future Improvements**

- Conversation Management: Implement conversation_id to support multiple sessions.
- Styling Enhancements: Improve the UI with libraries like Bootstrap or Material-UI.
- Authentication: Add user login to personalize chat history.
- Data Persistence: Store and load chat history from the database based on user sessions.