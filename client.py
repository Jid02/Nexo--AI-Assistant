from openai import OpenAI

# pip install openai

# Initialize client with your API key
client = OpenAI(
    api_key="your_api_key_here"  # Replace with your actual key
)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

# Print response
print(completion.choices[0].message.content)
