"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyB9MWkHiT0-z1hAhxSkyt-ZFhoiOjgjQEo")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Your name is leo, a mental health chatbot. Your task is to assist users in their questions related to mental health, if not do not respond and just say, its out of my turf. Be in your character no matter what and continue conversations to get max info about the patient status. Keep your answers short and understandable."
)

chat_session = model.start_chat(
    history=[
    ]
)

while True:
    user_input = input("Enter your message (type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("Stopping the chat session.")
        break

    response = chat_session.send_message(user_input)
    print("AI Response:", response.text)