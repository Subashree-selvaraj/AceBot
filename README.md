
# 🤖 AceBot – Your AI-Powered Interview Coach

AceBot is an AI-driven interview preparation assistant that simulates **real interview conversations** and provides **instant, adaptive feedback**.

Instead of static question lists, AceBot interacts with you like a real interviewer—asking follow-up questions, adapting based on your responses, and helping you refine your answers with confidence.

---

## 🎯 What Problem Does AceBot Solve?

Traditional interview prep often:
- Feels repetitive and predictable
- Lacks real-time feedback
- Doesn’t adapt to your responses
- Separates technical and non-technical practice

AceBot bridges this gap by offering a **dynamic, AI-powered interview experience** that feels natural, interactive, and role-specific.

---

## 🚀 Key Features

- 🗣️ Real-time AI-driven interview simulation  
- 🔄 Adaptive follow-up questions based on your answers  
- 💬 Instant feedback and response refinement  
- 💻 Supports both **technical & non-technical roles**  
- ⚡ Lightweight, fast, and easy to run locally  
- 🧠 Feels like practicing with a real interviewer  

---

## 🛠 Tech Stack

### AI & LLMs
- LangChain – Structured and intelligent question generation  
- Ollama – Local LLM orchestration for optimized performance  
- Large Language Models:
  - LLaMA 3.1  
  - Gemma 2  
  - Phi-3  

### Frontend / UI
- Streamlit  

### Backend / Core
- Python  

---

## 🧠 How AceBot Works

1. User selects interview type (technical / non-technical)
2. AceBot generates role-specific questions using LangChain
3. Responses are analyzed by LLMs
4. Follow-up questions adapt dynamically
5. Instant feedback helps improve answer quality

---

## 🎥 Demo


https://github.com/user-attachments/assets/04fa666b-c5e2-4b69-bb2e-348a8ea19fbc



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AceBot.git
cd AceBot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Setup Ollama & Models
ollama pull llama3.1
ollama pull gemma2
ollama pull phi3


Make sure Ollama is running:

ollama serve

4️⃣ Run the application
streamlit run app.py
