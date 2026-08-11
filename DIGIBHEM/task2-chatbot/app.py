
"""
DigiBhemBot - Free Local AI Chatbot
===================================

FastAPI + Ollama

Features:
- Free local LLM
- No OpenAI API
- Conversation memory
- Fast common responses
- Stable response generation
- Error handling
- Health check

Run:
    uvicorn app:app --reload
"""

from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from ollama import chat


# =========================================================
# CONFIG
# =========================================================

BOT_NAME = "DigiBhemBot"

# Smaller and faster local model
MODEL_NAME = "gemma4:e4b"


# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="DigiBhemBot API",
    description="Free local AI chatbot using Ollama",
    version="5.0.0"
)


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are DigiBhemBot, a smart, friendly and professional AI assistant.

You are part of a Digital Bhem AI/ML internship project.

Answer the user's question directly and completely.

IMPORTANT RESPONSE RULES:

- Never stop in the middle of a sentence.
- Never leave a list unfinished.
- Give a complete answer.
- For simple questions, keep answers short.
- For "explain" questions, give a clear and useful explanation.
- Use headings and bullet points when they improve readability.
- Do not unnecessarily repeat information.
- Remember the recent conversation context.
- Answer follow-up questions using the previous context.
- For programming questions, give complete working code.
- Explain code when useful.
- Do not pretend to be human.
- Your name is DigiBhemBot.
- Do not claim real-time information unless it is supplied by the application.

You can help with:

Artificial Intelligence
Machine Learning
Deep Learning
NLP
LLMs
Python
Programming
Web Development
Data Science
Software Development
General Knowledge
Education
"""


# =========================================================
# REQUEST
# =========================================================

class ChatRequest(BaseModel):

    message: str

    conversation: list[dict] = Field(
        default_factory=list
    )


# =========================================================
# RESPONSE
# =========================================================

class ChatResponse(BaseModel):

    reply: str


# =========================================================
# QUICK RESPONSES
# =========================================================

def get_quick_response(message: str):

    text = message.lower().strip()


    # -----------------------------------------------------
    # Greetings
    # -----------------------------------------------------

    if text in {
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii"
    }:

        return (
            "Hi! 👋 I'm DigiBhemBot. "
            "How can I help you today?"
        )


    # -----------------------------------------------------
    # Bot name
    # -----------------------------------------------------

    if (
        "what is your name" in text
        or "what's your name" in text
        or "who are you" in text
    ):

        return (
            "I'm DigiBhemBot 🤖, "
            "your AI assistant."
        )


    # -----------------------------------------------------
    # Date
    # -----------------------------------------------------

    date_phrases = [

        "today date",
        "today's date",
        "todays date",
        "what is today's date",
        "what is todays date",
        "what is the date today",
        "what date is today",
        "current date"

    ]


    if any(
        phrase in text
        for phrase in date_phrases
    ):

        now = datetime.now()

        return (
            f"Today is "
            f"{now.strftime('%A, %B %d, %Y')}."
        )


    # -----------------------------------------------------
    # Time
    # -----------------------------------------------------

    time_phrases = [

        "current time",
        "what time is it",
        "what is the time",
        "time now",
        "what's the time"

    ]


    if any(
        phrase in text
        for phrase in time_phrases
    ):

        now = datetime.now()

        return (
            f"The current time is "
            f"{now.strftime('%I:%M %p')}."
        )


    # -----------------------------------------------------
    # Goodbye
    # -----------------------------------------------------

    if text in {
        "bye",
        "goodbye",
        "see you",
        "see you later"
    }:

        return (
            "Goodbye! 👋 "
            "Have a great day!"
        )


    return None


# =========================================================
# AI RESPONSE
# =========================================================

def get_ai_response(
    message: str,
    conversation: list[dict]
):

    # -----------------------------------------------------
    # Fast response
    # -----------------------------------------------------

    quick = get_quick_response(message)

    if quick:

        return quick


    # -----------------------------------------------------
    # Prepare messages
    # -----------------------------------------------------

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]


    # Keep recent conversation only
    for item in conversation[-12:]:

        role = item.get("role")

        content = item.get("content")


        if (
            role in {"user", "assistant"}
            and content
        ):

            messages.append({

                "role": role,

                "content": str(content)

            })


    # Current user message
    messages.append({

        "role": "user",

        "content": message

    })


    # -----------------------------------------------------
    # Ollama generation
    # -----------------------------------------------------

    response = chat(

        model=MODEL_NAME,

        messages=messages,

        options={

            # Natural responses
            "temperature": 0.7,

            # Large enough for detailed explanations
            # without allowing uncontrolled generation.
            "num_predict": 4096

        },

        # Keep model loaded for faster next request
        keep_alive="10m"

    )


    answer = response.message.content


    if not answer:

        raise RuntimeError(
            "Ollama returned an empty response."
        )


    return answer.strip()


# =========================================================
# HOME PAGE
# =========================================================

@app.get("/")
def home():

    return FileResponse(
        "static/index.html"
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health():

    return {

        "status": "online",

        "bot": BOT_NAME,

        "version": "5.0.0",

        "model": MODEL_NAME,

        "provider": "Ollama Local LLM",

        "api": "FastAPI"

    }


# =========================================================
# CHAT
# =========================================================

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat_endpoint(
    request: ChatRequest
):

    message = request.message.strip()


    if not message:

        return ChatResponse(

            reply="Please type a message. 🙂"

        )


    try:

        reply = get_ai_response(

            message,

            request.conversation

        )


        return ChatResponse(

            reply=reply

        )


    except Exception as error:

        # Print actual error in terminal
        print()
        print("=" * 70)
        print("DIGIBHEMBOT / OLLAMA ERROR")
        print("=" * 70)
        print(repr(error))
        print("=" * 70)
        print()


        return ChatResponse(

            reply=(
                "I couldn't generate the AI response. "
                "Please make sure Ollama is running "
                "and the local model is available."
            )

        )


# =========================================================
# STATIC FILES
# =========================================================

app.mount(

    "/static",

    StaticFiles(
        directory="static"
    ),

    name="static"

)

