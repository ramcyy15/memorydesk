<div align="center">

# 🧠 MemoryDesk

### An AI help desk that actually *remembers*.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-8E75B2?logo=googlegemini&logoColor=white)
![Supabase](https://img.shields.io/badge/DB-Supabase%20%2B%20pgvector-3FCF8E?logo=supabase&logoColor=white)
![Cost](https://img.shields.io/badge/cost-%240.00-brightgreen)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

</div>

---

## ✨ What is MemoryDesk?

Most chatbots forget you the moment the conversation ends. **MemoryDesk doesn't.**

MemoryDesk is an AI-powered support desk with **long-term memory**. It stores past conversations as vector embeddings and pulls up the relevant history whenever a customer comes back, so it can answer with context:

> *"Hi again! Last week you had trouble with your billing address. Is this about the same issue?"*

## 🚀 Features

- 💬 **Chat with an AI agent** powered by Google Gemini
- 🧠 **Long-term memory**: conversations are embedded and saved, so nothing is forgotten
- 🔎 **Semantic search**: finds relevant past interactions by meaning, not just keywords (pgvector)
- 💸 **100% free stack**: runs entirely on free tiers

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 🐍 |
| LLM + Embeddings | Google Gemini (AI Studio free tier) |
| Database | Supabase (Postgres + pgvector) |
| Secrets | python-dotenv |

## ⚡ Quick Start

```powershell
# 1. Clone
git clone https://github.com/ramcyy15/memorydesk.git
cd memorydesk

# 2. Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key to a .env file
echo "GEMINI_API_KEY=your-key-here" > .env

# 5. Say hello to Gemini 👋
python hello_gemini.py
```

> 🔑 Get a free API key at [Google AI Studio](https://aistudio.google.com/).

## 🗺️ Roadmap

- [x] **Phase 0**: Project setup
- [x] **Phase 1**: Connect to Gemini API
- [ ] **Phase 2**: Supabase database + pgvector
- [ ] **Phase 3**: Embeddings & memory storage
- [ ] **Phase 4**: Memory recall in conversations
- [ ] **Phase 5**: Help desk interface

## ⚠️ Note

This is a learning project. It uses **fake customer data only**, since free-tier API data may be used by the provider.

---

<div align="center">

Made with ☕ and curiosity by **[ramcyy15](https://github.com/ramcyy15)**

</div>
