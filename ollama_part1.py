from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceEndpoint
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AceBot - Interview Prep Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title and Description
st.title("🤖 AceBot - Interview Prep Assistant")
st.markdown("### Get ready to ace your interview! Ask me anything related to job interviews. 💼")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history
st.markdown("### 🗨️ Chat History:")
for message in st.session_state.history:
    user_msg = f'<div class="chat-message user-message"><strong>You:</strong> {message["query"]}</div>'
    bot_msg = f'<div class="chat-message bot-message"><strong>AceBot:</strong> {message["response"]}</div>'
    st.markdown(user_msg, unsafe_allow_html=True)
    st.markdown(bot_msg, unsafe_allow_html=True)

# Input Box
input_txt = st.text_input("Enter your question here...")

# LangChain Setup with Hugging Face
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is AceBot."),
    ("user", "User query: {query}")
])

llm = HuggingFaceEndpoint(
    repo_id="gpt2",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.7
)


output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process User Input
if input_txt:
    response = chain.invoke({"query": input_txt})
    st.session_state.history.append({"query": input_txt, "response": response})

    st.markdown("### 🤔 Your Question:")
    st.write(input_txt)
    st.markdown("### 💡 AceBot's Response:")
    st.write(response)
