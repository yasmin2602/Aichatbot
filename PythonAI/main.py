import openai

# Sett API-nøkkelen din her
openai.api_key = "OpenAI API Key"

def chat_with_gpt(prompt):
    try:
        # Opprett et API-kall med riktig format
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Returner svaret fra modellen
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Chatbot is running. Type 'quit', 'exit', or 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
