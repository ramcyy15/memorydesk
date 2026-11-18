from pathlib import Path
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import math
from supabase import create_client, Client

# Functions Initialization
def cosine_similarity(a,b):
    dot = sum(x*y for x,y in zip(a,b))
    legth_a = math.sqrt(sum(x*x for x in a))
    legth_b = math.sqrt(sum(x*x for x in b))
    return dot / (legth_a * legth_b)
    
    

load_dotenv()
# Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)

# Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=gemini_api_key)

# Documents chunks
base_dir = Path("./docs")
all_items = base_dir.glob("**/*.md")
all_chunks = []

for file_path in all_items:
    content = Path.read_text(file_path, encoding="utf-8")
    # print(content)

    raw_pieces = content.split("## ")
    # print(raw_pieces)
    # print(len(raw_pieces))

    chunk_counter = 1  # numbering restarts at 1 for every file

    for piece in raw_pieces[1:]:
        lines = piece.splitlines()  # one section -> list of its lines

        heading = lines[0].strip()

        text = "\n".join(lines[1:]).strip()

        # Save this section as one chunk (a dictionary)
        all_chunks.append({
            "source": file_path.name,        
            "chunk_number": chunk_counter,   
            "heading": heading,
            "content": text,
        })
        chunk_counter += 1 

print(f"Total chunks collected: {len(all_chunks)}")
print(all_chunks[5])  

# Embedding it to gemini
text_to_embed = []

for chunk in all_chunks:

    text_to_embed.append([chunk["heading"], chunk["content"]])
    # print(f"Appended: {chunk["heading"]} & {chunk["text"]}")

# print(len(text_to_embed))
# print(text_to_embed[0])

response = client.models.embed_content(
    model='gemini-embedding-001',
    contents=text_to_embed,
    config=types.EmbedContentConfig(output_dimensionality=768, task_type="RETRIEVAL_DOCUMENT")
)
print(len(response.embeddings))
for chunk, emb in zip(all_chunks, response.embeddings):
    chunk['embedding'] = emb.values
    # print(all_chunks[0]["heading"])
    # print(len(all_chunks[0]["heading"]))

rows = []

for chunk in all_chunks:
    rows.append({
        "source": chunk["source"],
        "chunk_number": chunk["chunk_number"],
        "heading": chunk["heading"],
        "content": chunk["content"],
        "embedding": chunk["embedding"]
    })

data = supabase.table("doc_chunks").upsert(rows, on_conflict = "source,chunk_number" ).execute()

print(f"Succesfully: {len(data.data)}")



