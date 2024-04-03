import openai
from dotenv import load_dotenv
import os

# Load your OpenAI API key from an environment file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

class ChatEnvironment:
    def __init__(self):
        # Initialize with empty conversation history
        self.conversation_history = []

    def update_conversation_history(self, user_input, bot_response):
        # Append the latest exchange to the conversation history
        self.conversation_history.append(f"You: {user_input}")
        self.conversation_history.append(f"Bot: {bot_response}")

class ChatAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key  # Set the API key globally for the openai library

    def generate_response(self, prompt):
        # Use the OpenAI API to generate a response using the chat model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust this to the specific chat model you intend to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']



def main():
    env = ChatEnvironment()
    agent = ChatAgent(openai_api_key)

    print("Welcome! Talk to me like you would to a teacher or a friend. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'bye':
            print("Bot: It was great talking to you. Bye!")
            break

        # Generate a prompt that includes conversation history
        prompt = "\n".join(env.conversation_history[-6:]) + f"\nYou: {user_input}\nBot:"
        response = agent.generate_response(prompt)
        
        print(f"Bot: {response}")
        env.update_conversation_history(user_input, response)

if __name__ == "__main__":
    main()
