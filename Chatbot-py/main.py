# pip install google-generativeai
# pip install --force-reinstall google-generativeai

import google.generativeai as genai
import sys

genai.configure(api_key="Colocar sua api key")

# Create the model
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
)

chat_session = model.start_chat(
    history=[
    ]
)

if len(sys.argv) > 1:
    usuario_input = sys.argv[1]
    response = chat_session.send_message({usuario_input})
else:
    print("va toma no cu")

print(response.text)