import openai
openai.api_key = "DAAAAAAAAAAAAAAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNN MYYYYYYYYYYYY BILLLIIIIIIINNNNNNNNNNGGGGGGGGGGGG STTTTTTTAAAAAAAAAATTTTTTTTTTUUUUUUUUUUUUUSSSSSSSSSSSSSS????????????? btw its over use your api key :("

try:
    openai.Model.list()
except Exception as e:
    print("❌ Failed to connect to OpenAI:", e)
    exit()

# Chat function
def chat_with_gpt(chat_log):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
            timeout=15
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error communicating with OpenAI API:", e)
        return "Sorry, I couldn't reach the server."

chat_log = []
n_remembered = 5 

if __name__ == "__main__":
    print("💬 Chatbot is ready! Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        chat_log.append({'role': 'user', 'content': user_input})

        if len(chat_log) > n_remembered * 2:
            chat_log = chat_log[-n_remembered * 2:]

        response = chat_with_gpt(chat_log)
        print("Bot:", response)

        chat_log.append({'role': 'assistant', 'content': response})