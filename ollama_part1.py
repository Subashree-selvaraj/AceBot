import streamlit as st
from openai import OpenAI
import os

# -------------------------
# Setup API client
# -------------------------
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# -------------------------
# Streamlit Page Config
# -------------------------
st.set_page_config(page_title="AceBot - ChatGPT Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AceBot - ChatGPT-Quality Assistant")
st.markdown("Ask me anything about interview preparation!")

# -------------------------
# Initialize Session State
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# Display Chat History
# -------------------------
for i, chat in enumerate(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AceBot:** {chat['assistant']}")

# -------------------------
# Input Box
# -------------------------
query = st.text_input("Type your question and press Enter:")

# -------------------------
# Process User Input
# -------------------------
if query:
    with st.spinner("Thinking..."):
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, professional interview preparation assistant."},
                {"role": "user", "content": query}
            ]
        )
        response = completion.choices[0].message.content

    # Save to history
    st.session_state.history.append({"user": query, "assistant": response})

    # Display
    st.markdown(f"**You:** {query}")
    st.markdown(f"**AceBot:** {response}")
