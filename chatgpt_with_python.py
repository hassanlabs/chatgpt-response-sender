import os
import openai

# Set your OpenAI API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to interact with GPT-3.5-turbo
def ask_chatgpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Free-tier model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    user_input = input("Ask ChatGPT: ")
    reply = ask_chatgpt(user_input)
    print("ChatGPT Reply:", reply)
