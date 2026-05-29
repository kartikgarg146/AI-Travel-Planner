<div align="center">

# 🌍 AI Travel Planner

### *Your Intelligent Travel Companion — Powered by AI*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3-00A67E?style=for-the-badge)](https://groq.com)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://ai-travel-planner-kartik.streamlit.app)

**Plan smarter. Travel better. No more tab-hopping.**

[🌐 Try the Live App](https://ai-travel-planner-kartik.streamlit.app) · [📖 Report a Bug](https://github.com/your-username/AI-Travel-Planner/issues) · [✨ Request a Feature](https://github.com/your-username/AI-Travel-Planner/issues)

</div>

---

## 📸 Preview

> *Chat with an AI that understands your travel style — not just your destination.*

```
You:     "Plan a 7-day budget trip to Japan for 5 people"
AI:      "Great choice! 🇯🇵 Here's a day-by-day itinerary for Tokyo, Kyoto & Osaka,
          keeping your budget under ₹1.2L. Want me to add hotel options too?"
```

---

## 🎯 What Is This?

AI Travel Planner is a **conversational travel assistant** that replaces hours of research with a simple chat. Instead of juggling 10 browser tabs, just describe your trip — and let the AI handle the rest.

It remembers your preferences, asks the right follow-up questions, and generates complete itineraries with hotel suggestions and budget breakdowns — all in natural language.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Chat-Based Planning** | Describe your trip in plain English — no forms, no dropdowns |
| 🧠 **Smart Memory** | Remembers destination, budget, travel dates & preferences across the conversation |
| 🤖 **AI-Powered Recommendations** | Uses Groq's LLaMA 3 for fast, intelligent, context-aware responses |
| 📄 **RAG PDF Support** | Upload travel guides, brochures, or docs — the AI reads and uses them |
| ⚡ **Dynamic Itinerary Generation** | Proactively asks for missing info before building your plan |
| 💰 **Budget Planning** | Get cost estimates tailored to your budget and travel style |
| 🏨 **Hotel Suggestions** | Curated accommodation options based on your preferences |


---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **UI / Frontend** | [Streamlit](https://streamlit.io) |
| **LLM** | [Groq API](https://groq.com) — LLaMA 3 (ultra-fast inference) |
| **RAG Framework** | [LangChain](https://langchain.com) |
| **Vector Store** | [FAISS](https://faiss.ai) |
| **Embeddings** | [HuggingFace Transformers](https://huggingface.co) |
| **Language** | Python 3.10+ |
| **Deployment** | [Streamlit Cloud](https://streamlit.io/cloud) |

---

## 📂 Project Structure

```
AI-Travel-Planner/
│
├── travel_agent.py        # 🧠 Main application — AI agent + Streamlit UI
├── requirements.txt       # 📦 Python dependencies
├── .env                   # 🔐 API keys (not committed — see setup)
├── .gitignore             # 🚫 Excludes .env, __pycache__, etc.
└── README.md              # 📖 You're here!
```

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.10 or higher
- A free [Groq API key](https://console.groq.com)

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/AI-Travel-Planner.git
cd AI-Travel-Planner
```

### Step 2 — Create a virtual environment

```bash
# Create environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 💡 Get your free API key at [console.groq.com](https://console.groq.com)

### Step 5 — Run the app

```bash
streamlit run travel_agent.py
```

Open your browser at `http://localhost:8501` and start planning! 🎉

---

## 🌐 Deployment on Streamlit Cloud

1. **Push** your code to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. In **Settings → Secrets**, add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

4. Click **Deploy** — your app will be live in minutes 🚀

> ✅ **Live demo:** [ai-travel-planner-kartik.streamlit.app](https://ai-travel-planner-kartik.streamlit.app)

---

## 📊 Why AI Travel Planner?

| Feature | Traditional Apps | AI Travel Planner |
|---|---|---|
| Planning Style | Manual, form-based | Conversational AI |
| Personalization | Limited / template-based | High — adapts to your needs |
| Time to Itinerary | Hours of research | Minutes |
| PDF/Document Support | ❌ | ✅ RAG-powered |
| Budget Awareness | Partial | ✅ Fully integrated |
| Follow-up Questions | ❌ | ✅ Proactively asks |
| Intelligence Level | Rule-based | LLM-powered |

---

## 🔮 Roadmap

- [ ] 🎙️ Voice-based interaction
- [ ] ✈️ Real-time flight & hotel price APIs (Skyscanner, Booking.com)
- [ ] 🔑 User authentication & saved itineraries
- [ ] 🌤️ Live weather integration per destination
- [ ] 📱 Mobile app (React Native)
- [ ] 🗺️ Interactive map view of itineraries
- [ ] 💱 Multi-currency budget support

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request 🎉
```

Please follow [conventional commits](https://www.conventionalcommits.org/) and open an issue before starting major changes.

---

<div align="center">

**⭐ If you found this useful, give it a star — it helps a lot!**

*Built with ❤️ to make travel planning intelligent and fun.*

</div>
