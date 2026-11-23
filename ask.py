from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
# Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)

# Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=gemini_api_key)

# question = "Do you integrate with Shopify?"

def answer_question(question):
    context = ""
    embedding = client.models.embed_content(
        model='gemini-embedding-001',
        contents=question,
        config=types.EmbedContentConfig(output_dimensionality=768, task_type="RETRIEVAL_QUERY")
    )

    question_vector = embedding.embeddings[0].values
    result = supabase.rpc( "match_doc_chunks", { "query_embedding":question_vector,  "match_count": 3} ).execute()


    for chunk in result.data:
        context += f"[{chunk["source"]} #{chunk["chunk_number"]}]\n"
        #print("Source & id succesfully concat")
        context += f"{chunk["content"]}\n\n"
        #print("Content succesfully concat")




    content = f"SOURCES:\n{context}\n\nQUESTION:\n{question}"
    system_prompt = "You are a customer support agent for a product called MemoryDesk, your tone must be professional and friendly. Maintain a friendly and approachable personality, when responding be straightforward and direct to the query.\n\nMANDAORTY RULES:\n1.) Answer only using the information in the SOURCES.\n2.) After every claim, put the label of the source it came from, in square brackets, exactly as written.\n3.) If the SOURCES don't contain the answer, say you don't know. Never guess or use outside knowledge.\n4.)I want the answer in plain text."

    response = client.models.generate_content(
        model = 'gemini-3.5-flash',
        contents=content,
        config = types.GenerateContentConfig(
            system_instruction = system_prompt
        ),
    )

    return response.text

# if __name__ == "__main__":
#     answer_question("Can I get my money back?")

