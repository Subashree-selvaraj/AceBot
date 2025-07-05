from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceEndpoint
import streamlit as st

# Page Config
st.set_page_config(page_title="AceBot", page_icon="🤖")

st.title("🤖 AceBot - Interview Prep Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

# Show chat history
for m in st.session_state.history:
    st.markdown(f"**You:** {m['query']}")
    st.markdown(f"**AceBot:** {m['response']}")

input_txt = st.text_input("Ask me anything about interviews:")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "User query: {query}")
])

llm = HuggingFaceEndpoint(
    repo_id="bigscience/bloomz-560m",  # ✅ No license needed
    task="text-generation",
    max_new_tokens=256,
    temperature=0.7
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_txt:
    response = chain.invoke({"query": input_txt})
    st.session_state.history.append({"query": input_txt, "response": response})
    st.markdown("**Response:**")
    st.write(response)
