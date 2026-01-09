import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("API_KEY"),
    model_id="llama-3.3-70b-versatile",
)

def check_password_length(password: str) -> str:
    """Checks if a password is at least 8 characters long."""
    return "Strong" if len(password) >= 8 else "Weak"

agent = ChatAgent(
    chat_client=client,
    name="security-agent",
    instructions="You are a security assistant. Use the check_password_length tool.",
    tools=[check_password_length]
)