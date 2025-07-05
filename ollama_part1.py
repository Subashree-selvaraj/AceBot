import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Page Configuration
st.set_page_config(
    page_title="AceBot - Interview Prep Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 AceBot - Interview Prep Assistant")
st.markdown("Get ready to ace your interview! Ask me anything.")

# Load tokenizer and model (load only once)
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("bigscience/bloomz-560m")
    model = AutoModelForCausalLM.from_pretrained("bigscience/bloomz-560m")
    return tokenizer, model

tokenizer, model = load_model()

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
for message in st.session_state.history:
    st.markdown(f"**You:** {message['user']}")
    st.markdown(f"**AceBot:** {message['bot']}")

# Input box
user_input = st.text_input("Type your question and press Enter:")

# Process input
if user_input:
    # Encode input prompt
    inputs = tokenizer(user_input, return_tensors="pt")

    # Generate text
    outputs = model.generate(
        **inputs,
        max_length=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Add to history
    st.session_state.history.append({
        "user": user_input,
        "bot": response
    })

    # Display latest response
    st.markdown("### 🤔 Your Question")
    st.write(user_input)
    st.markdown("### 💡 AceBot's Response")
    st.write(response)
