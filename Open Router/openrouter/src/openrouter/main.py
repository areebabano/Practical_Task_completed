# my_openrouter_agent.py

import asyncio
import nest_asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Enable nested async for CLI
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openai/gpt-3.5-turbo"

# Disable tracing
set_tracing_disabled(disabled=True)

# Set up OpenAI client using OpenRouter
client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)

# Create your agent
agent = Agent(
    name="Helper Areeba",
    instructions="You are a helpful Python expert. Solve the user's coding problems.",
    model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
)

# Chat loop
async def main():
    print("👋🏻 Hello Areeba! Ask your Python questions (or type 'exit' to quit).\n")
    while True:
        user_input = input("👤 Areeba: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting... See you soon! 😊")
            break
        result = await Runner.run(agent, user_input)
        print("🤖:", result.final_output.strip(), "\n")

if __name__ == "__main__":
    asyncio.run(main())
