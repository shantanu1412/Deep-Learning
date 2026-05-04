from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("=== Simple AI App (Groq) ===")

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    while True:
        user_input = input("\nAsk something (type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("\nAI:", response.choices[0].message.content)

if __name__ == "__main__":
    main()