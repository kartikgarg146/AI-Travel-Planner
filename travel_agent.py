# =====================================
# FINAL HYBRID AI TRAVEL CHATBOT
# (Chat + Sidebar + Memory + RAG)
# =====================================

import streamlit as st
from groq import Groq
import json
import os
from dotenv import load_dotenv
load_dotenv()


# RAG imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="🌍 Travel AI", layout="wide")
st.title("🌍 AI Travel Planner")

# Load API key securely
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Missing GROQ_API_KEY. Set it in environment variables.")
    st.stop()

client = Groq(api_key=api_key)

# -----------------------------
# SESSION STATE
# -----------------------------
if "memory" not in st.session_state:
    st.session_state.memory = {
        "country": "",
        "cities": "",
        "days": "",
        "budget": ""
    }

if "chat_summary" not in st.session_state:
    st.session_state.chat_summary = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "cities_suggested" not in st.session_state:
    st.session_state.cities_suggested = False

# -----------------------------
# SIDEBAR INPUTS (SYNC MEMORY)
# -----------------------------
st.sidebar.header("✈️ Trip Details")

sb_country = st.sidebar.text_input("Country")
sb_cities = st.sidebar.text_input("Cities")
sb_days = st.sidebar.number_input("Days", 1, 30, 5)
sb_budget = st.sidebar.text_input("Budget")

# Update memory from sidebar (priority)
if sb_country:
    st.session_state.memory["country"] = sb_country
if sb_cities:
    st.session_state.memory["cities"] = sb_cities
if sb_days:
    st.session_state.memory["days"] = str(sb_days)
if sb_budget:
    st.session_state.memory["budget"] = sb_budget

# -----------------------------
# PDF (RAG)
# -----------------------------
uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    st.session_state.vector_db = FAISS.from_documents(chunks, embedding)
    st.success("PDF Ready!")

# -----------------------------
# GROQ CALL
# -----------------------------
def ask_groq(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# -----------------------------
# UPDATE MEMORY FROM CHAT
# -----------------------------
def update_memory(user_input):
    prompt = f"""
Extract structured info from input.

Input: {user_input}

Return JSON:
country, cities, days, budget
Only fill if present.
"""

    try:
        data = json.loads(ask_groq(prompt))
        for key in st.session_state.memory:
            if data.get(key):
                st.session_state.memory[key] = data[key]
    except:
        pass


# -----------------------------
# CHAT SUMMARY (LIGHT MEMORY)
# -----------------------------
def update_summary(user, bot):
    prompt = f"""
Summarize conversation briefly (max 50 words).

Previous:
{st.session_state.chat_summary}

New:
User: {user}
Bot: {bot}
"""
    st.session_state.chat_summary = ask_groq(prompt)


# -----------------------------
# MAIN CHAT AGENT
# -----------------------------
def chat_agent(user_input):

    update_memory(user_input)

    memory = st.session_state.memory

    # RAG
    rag_context = ""
    if st.session_state.vector_db:
        docs = st.session_state.vector_db.similarity_search(user_input, k=2)
        rag_context = "\n".join([d.page_content for d in docs])

    # Decide behavior
    need_more_info = not memory["country"] or not memory["days"]

    # Suggest cities ONLY ONCE
    suggest_cities = False
    if memory["country"] and not memory["cities"] and not st.session_state.cities_suggested:
        suggest_cities = True
        st.session_state.cities_suggested = True

    prompt = f"""
You are a smart travel planner.

User Input: {user_input}

Memory:
{memory}

Chat Summary:
{st.session_state.chat_summary}

Context:
{rag_context}

Rules:
- Keep response SHORT (max 120 words)
- Use bullet points
- DO NOT ask same question again
- If cities missing → suggest once
- If enough data → generate itinerary
- If missing critical info → ask only 1 question

Task:
"""

    if need_more_info:
        prompt += "Ask for missing key info."
    elif suggest_cities:
        prompt += "Suggest best cities."
    else:
        prompt += "Generate optimized travel plan (itinerary + hotel + food + budget short)."

    return ask_groq(prompt)


# -----------------------------
# CHAT UI
# -----------------------------
user_input = st.chat_input("Ask anything about your trip...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    reply = chat_agent(user_input)

    st.session_state.messages.append(("bot", reply))

    update_summary(user_input, reply)

# -----------------------------
# DISPLAY CHAT
# -----------------------------
for role, msg in st.session_state.messages:
    with st.chat_message("assistant" if role == "bot" else "user"):
        st.write(msg)

# -----------------------------
# DEBUG MEMORY
# -----------------------------
st.sidebar.markdown("### 🧠 Memory")
st.sidebar.json(st.session_state.memory)