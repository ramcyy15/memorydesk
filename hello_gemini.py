from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key = gemini_api_key)

response_1 = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents='Hello!',
)

print(response_1)

client.close()

