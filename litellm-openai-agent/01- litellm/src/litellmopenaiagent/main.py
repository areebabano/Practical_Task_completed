from litellm import completion
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Get OpenRouter API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("🧪 OpenRouter API Key:", OPENROUTER_API_KEY)

def chat_with_model(model_name: str, user_input: str):
    response = completion(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful and polite assistant."},
            {"role": "user", "content": user_input}
        ],
        api_key=OPENROUTER_API_KEY,
        api_base="https://openrouter.ai/api/v1"
    )
    print("\n🤖 Assistant:", response['choices'][0]['message']['content'])

def main():
    print("🤖 Welcome to Interactive Chat with LLMs via OpenRouter!\n")
    print("Available Models:")
    print("1. openrouter/deepseek/deepseek-r1:free")
    print("2. openrouter/meta-llama/llama-3.3-8b-instruct:free")
    print("3. openrouter/mistralai/devstral-small:free\n")

    choice = input("👉 Enter model number (1/2/3): ").strip()
    model_map = {
        "1": "openrouter/deepseek/deepseek-r1:free",
        "2": "openrouter/meta-llama/llama-3.3-8b-instruct:free",
        "3": "openrouter/mistralai/devstral-small:free",
    }

    selected_model = model_map.get(choice)
    if not selected_model:
        print("⚠️ Invalid model selection.")
        return

    user_prompt = input("🧑 You: ")

    chat_with_model(selected_model, user_prompt)

if __name__ == "__main__":
    main()
