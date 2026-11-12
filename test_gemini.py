import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

print("API Key encontrada:", bool(api_key))

client = genai.Client(api_key=api_key)

print("Enviando requisição...")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Olá, tudo bem?"
)

print(response.text)