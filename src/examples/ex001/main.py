from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model('google_genai:gemini-3.6-flash')

print(llm, type(llm))

response = llm.invoke('Olá, tudo bem?')

print(response)