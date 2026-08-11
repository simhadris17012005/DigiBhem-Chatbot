# 🤖 DigiBhemBot — AI Chatbot

DigiBhemBot is a **free, local AI chatbot** developed as part of the **Digital Bhem AI/ML Internship — Task 2: Create a Chatbot**.

The project uses **FastAPI** for the backend, **Ollama + Gemma 4** for local AI responses, and a modern **HTML/CSS/JavaScript** interface for chatting.

## ✨ Features

* 🤖 AI-powered conversational chatbot
* 🆓 Runs locally without OpenAI API credits
* 🧠 Powered by Ollama + Gemma 4
* 💬 Conversation context and follow-up questions
* ⚡ Fast responses for common questions
* 📅 Current date and time responses
* 🧑‍💻 Programming and AI/ML explanations
* 🌐 FastAPI REST API
* 🎨 Modern web-based chat interface
* 🛡️ Local processing — no API key required for the chatbot
* 📱 Responsive chat interface

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Ollama**
* **Gemma 4**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Uvicorn**
* **Pydantic**

## 📁 Project Structure

```text
DigiBhem-Chatbot/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── Procfile
├── README.md
├── LICENSE
│
└── static/
    └── index.html
```

## ⚙️ Requirements

Before running the project, install:

* Python 3.10+
* Ollama
* Git

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/simhadris17012005/DigiBhem-Chatbot.git
```

### 2. Open the project

```bash
cd DigiBhem-Chatbot
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
venv\Scripts\activate
```

### 5. Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 6. Install the Ollama model

```powershell
ollama pull gemma4:e4b
```

### 7. Start the FastAPI server

```powershell
python -m uvicorn app:app --reload
```

### 8. Open the chatbot

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## 💬 Example

```text
You: hi

DigiBhemBot:
Hi! 👋 I'm DigiBhemBot. How can I help you today?
```

Example AI/ML question:

```text
You: Explain machine learning
```

The chatbot generates a detailed explanation using the local Gemma model.

## 🔌 API

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "online",
  "bot": "DigiBhemBot",
  "version": "5.0.0",
  "model": "gemma4:e4b",
  "provider": "Ollama Local LLM",
  "api": "FastAPI"
}
```

### Chat

```http
POST /chat
```

Request:

```json
{
  "message": "Explain artificial intelligence",
  "conversation": []
}
```

Response:

```json
{
  "reply": "Artificial Intelligence is..."
}
```

## 🧠 How It Works

```text
User
  │
  ▼
Web Interface
  │
  ▼
FastAPI Backend
  │
  ▼
Ollama
  │
  ▼
Gemma 4 Local LLM
  │
  ▼
AI Response
  │
  ▼
Web Interface
```

The chatbot processes user messages through the FastAPI backend and sends them to the locally running Gemma 4 model through Ollama.

## 🔐 Privacy

DigiBhemBot is designed to run the AI model locally through Ollama.

No OpenAI API key is required for the chatbot.

Do not commit `.env` files, API keys, passwords, virtual environments, or local database files to GitHub.

## 🎯 Internship Task

**Program:** Digital Bhem AI/ML Internship

**Task:** Task 2 — Create a Chatbot

**Project:** DigiBhemBot

The project demonstrates the development of an AI chatbot with a Python backend and web-based frontend.

## 👨‍💻 Author

**Simhadri**

GitHub:
https://github.com/simhadris17012005

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.
