from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

# Page Configuration
st.set_page_config(page_title="AceBot - Interview Prep Assistant", page_icon="🤖", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
            color: #2c3e50;
            font-family: 'Arial', sans-serif;
        }
        .chat-history {
            background-color: #ffffff;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            max-height: 400px;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        .chat-message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 10px;
        }
        .user-message {
            background-color: #e8f4fd;
            text-align: right;
        }
        .bot-message {
            background-color: #f0f0f0;
            text-align: left;
        }
        .stTextInput input {
            border: 2px solid #3498db;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            padding: 8px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #2980b9;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🤖 AceBot - Interview Prep Assistant")
st.markdown("### Get ready to ace your interview! Ask me anything related to job interviews. 💼")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history in a box
st.markdown("### 🗨️ Chat History:")

for message in st.session_state.history:
    user_msg = f'<div class="chat-message user-message"><strong>You:</strong> {message["query"]}</div>'
    bot_msg = f'<div class="chat-message bot-message"><strong>AceBot:</strong> {message["response"]}</div>'
    st.markdown(user_msg, unsafe_allow_html=True)
    st.markdown(bot_msg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input Box at the Bottom
input_txt = st.text_input("Enter your question here...")

# LangChain Setup
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is AceBot."),
    ("user", "User query: {query}")
])
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process User Input and Save History
if input_txt:
    response = chain.invoke({"query": input_txt})
    st.session_state.history.append({"query": input_txt, "response": response})

    # Display Latest Interaction
    st.markdown("### 🤔 Your Question:")
    st.write(input_txt)
    st.markdown("### 💡 AceBot's Response:")
    st.write(response)
