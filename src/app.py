# src/app.py

import streamlit as st
from qa import load_qa_chain, ask

# Page config
st.set_page_config(
    page_title="Geospatial QA Tool",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 Geospatial QA Assistant")
st.caption("Ask anything about PostGIS, GDAL, CRS, OGC standards, and spatial testing.")

# Load QA chain once and cache it
@st.cache_resource
def get_chain():
    with st.spinner("Loading knowledge base..."):
        return load_qa_chain()

qa_chain = get_chain()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("📚 Sources"):
                for s in msg["sources"]:
                    st.markdown(f"- {s}")

# Chat input
if question := st.chat_input("e.g. How do I validate geometry in PostGIS?"):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get answer
    with st.chat_message("assistant"):
        with st.spinner("Searching docs..."):
            result = ask(qa_chain, question)

        st.markdown(result["answer"])

        if result["sources"]:
            with st.expander("📚 Sources"):
                for s in result["sources"]:
                    st.markdown(f"- {s}")

    # Save to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "sources": result["sources"],
    })