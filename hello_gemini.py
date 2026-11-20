from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key = gemini_api_key)


content = f"SOURCES:\n{context}\n\nQUESTION:\n{question}"
system_prompt = "You are a customer support agent for a product called MemoryDesk, your tone must be professional and friendly. Maintain a friendly and approachable personality, when responding be straightforward and direct to the query. "
        "MANDAORTY RULES:"
        "1.) Answer only using the information in the SOURCES."
        "2.) After every claim, put the label of the source it came from, in square brackets, exactly as written."
        "3.) If the SOURCES don't contain the answer, say you don't know. Never guess or use outside knowledge."

response = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents=content,
    config = types.GenerateContentConfig(
        system_instruction = system_prompt
    ),
)


print(response.text)

client.close()

