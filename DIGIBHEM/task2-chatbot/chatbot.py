
"""
Task-2: Create a Chatbot
Digital Bhem AI/ML Internship

DigiBhemBot - LLM-powered AI chatbot
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. "
        "Please add it to your .env file."
    )


# OpenAI client
client = OpenAI(api_key=api_key)


SYSTEM_INSTRUCTIONS = """
You are DigiBhemBot, a smart, friendly and helpful AI assistant.

Your job is to have natural conversations with users.

Guidelines:
- Give clear and accurate answers.
- Explain difficult concepts in simple language.
- For programming questions, provide working code and explanations.
- Help with AI, machine learning, Python, web development and general questions.
- If the user asks for a detailed explanation, provide a detailed answer.
- If the user asks for a short answer, keep it concise.
- Be friendly and professional.
- Do not claim to be a human.
- You are DigiBhemBot, an AI assistant created for the Digital Bhem internship project.
"""


def get_ai_response(conversation):
    """
    Send the conversation to the LLM and return the response.
    """

    response = client.responses.create(
        model="gpt-5.5",
        instructions=SYSTEM_INSTRUCTIONS,
        input=conversation,
    )

    return response.output_text


def build_chatbot():
    """
    Creates the chatbot configuration.
    """

    return {
        "name": "DigiBhemBot"
    }


def chat_loop():
    """
    Terminal-based chatbot loop.
    """

    bot = build_chatbot()

    print("=" * 60)
    print(f"🤖 {bot['name']} - AI Assistant")
    print("=" * 60)
    print("Ask me anything!")
    print("Type 'quit', 'exit' or 'bye' to stop.")
    print()

    conversation = []

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print(f"{bot['name']}: Goodbye! 👋")
            break

        conversation.append({
            "role": "user",
            "content": user_input
        })

        try:
            answer = get_ai_response(conversation)

            print(f"{bot['name']}: {answer}\n")

            conversation.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:

            print(
                f"{bot['name']}: Sorry, I couldn't process "
                "your request right now."
            )

            print(f"Error: {error}\n")


if __name__ == "__main__":
    chat_loop()

