import openai
openai.api_key = "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"
openai.api_base="https://openrouter.al/api/v1"
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
     print("Chatbot: Goodbye!")
     break
    response = openai.ChatCompletion.create(
     model="mistralai/mistral-7b-instruct",
     messages=
            {{"role": "system", "content": "You are a helpful and friendly At assistant."},
            {"role": "user", "content": user_input}
            }
    )
    reply= response['choices'][0]['message']['content'].strip()
    print("Chatbot: (reply)\n")
