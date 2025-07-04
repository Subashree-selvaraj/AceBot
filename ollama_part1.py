from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceEndpoint
import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="AceBot - Interview Prep Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS (optional, you can remove or adjust)
st.markdown("""
    <style>
        .chat-message {
            padding: 0.5rem;
            border-radius: 5px;
            margin-bottom: 0.5rem;
        }
        .user-message {
            background-color: #DCF8C6;
            text-align: left;
        }
        .bot-message {
            background-color: #F1F0F0;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🤖 AceBot - Interview Prep Assistant")
st.markdown("### Get ready to ace your interview! Ask me anything related to job interviews. 💼")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
st.markdown("### 🗨️ Chat History:")
for message in st.session_state.history:
    st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["query"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-message bot-message"><strong>AceBot:</strong> {message["response"]}</div>', unsafe_allow_html=True)

# Input box
input_txt = st.text_input("Enter your question here...")

# HuggingFaceEndpoint setup
huggingface_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
if not huggingface_token:
    st.error("❌ Hugging Face API token not found. Make sure you set it in Streamlit Secrets.")
    st.stop()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is AceBot."),
    ("user", "User query: {query}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Process input
if input_txt:
    try:
        response = chain.invoke({"query": input_txt})
        st.session_state.history.append({"query": input_txt, "response": response})

        st.markdown("### 🤔 Your Question:")
        st.write(input_txt)
        st.markdown("### 💡 AceBot's Response:")
        st.write(response)

    except Exception as e:
        st.error(f"❌ Error: {e}")
