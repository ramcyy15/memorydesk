from pydantic  import BaseModel
from typing import Literal, List
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os



load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=gemini_api_key)

class Fact(BaseModel):
    category: Literal ["account", "preference"]
    key: Literal ["company", "plan", "team_size", "reply_style", "language", "timezone"]
    value: str
    statement: str
    evidence_quote: str

def extract_facts(message:str):

    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction="""
You are a customer fact extraction system.

Your task is to extract facts about the customer from a single message.

RULES:
1. Extract only facts the customer explicitly states about themselves or their company.
2. Ignore questions, greetings, requests, and instructions.
3. Do not infer, assume, or invent facts.
4. Use only the predefined keys below. Never create new keys.
5. The evidence_quote must be copied word for word from the original message.
6. Every extracted fact must have direct supporting evidence.
7. If no qualifying facts are found, return an empty list.
8. Do not extract facts about other people.

ALLOWED KEYS:
- company
- plan
- team_size
- reply_style
- language
- timezone

OUTPUT FORMAT:
Return valid JSON only, without Markdown or explanations.

Example:
[
    {
        "key": "company",
        "value": "Example Company",
        "evidence_quote": "I work at Example Company."
    }
]

If no facts are found, return:
[]

IMPORTANT:
- Always use the exact allowed key names.
- Never invent or rename keys.
- Never paraphrase evidence_quote.
- Preserve the original meaning of extracted values.
"""
        , response_mime_type = "application/json",
        response_schema = list[Fact]
        )
    )

    return response.parsed


if __name__ == "__main__":
    facts = extract_facts("Hi! I run Bright Bakery. We're on the Pro plan and we have 4 people on the team. Also, please always reply in short bullet points, I read on my phone.")
    print(facts)

