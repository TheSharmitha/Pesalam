import openai
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"
user_input = input("You: ")
reply=""
response = openai.ChatCompletion.create(

        model="mistralai/mistral-7b-instruct", # or another supported model
        messages = [
        {"role": "system", "content": "You are an expert translator."},
        {"role": "user", "content": "English: Good morning\nFrench: Bonjour"},
        {"role": "user", "content": f"English: (user_input)\nFrench:"}]
    )
reply = response['choices'][0]['message']['content']
print (f"Chatbot: {reply}\n")
