from pathlib import Path
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key=gemini_api_key)

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
            "text": text,
        })
        chunk_counter += 1 

print(f"Total chunks collected: {len(all_chunks)}")
print(all_chunks[5])  

# # Embedding it to gemini
# response = client.models.embed_content(
# model='gemini-embedding-001',
# contents=value,
# config=types.EmbedContentConfig(output_dimensionality=768),
