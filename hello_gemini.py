from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key = gemini_api_key)

response = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents="What is MemoryDesk's refund policy?",
    config = types.GenerateContentConfig(
        system_instruction = "You are a customer support agent for a product called MemoryDesk, your tone must be professional and friendly. Maintain a friendly and approachable personality, when responsing straightforward and direct to the query"
    ),
)


print(response.text)

client.close()

