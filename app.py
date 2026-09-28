import streamlit as st

st.set_page_config(page_title="SnapRAG - Local AI", layout="centered")

st.title("⚡ SnapRAG: Zero-Trust Local AI")
st.markdown("Chat with your confidential documents locally. **Powered by Snapdragon NPU.**")

uploaded_file = st.file_uploader("Upload a highly confidential PDF", type="pdf")

if uploaded_file is not None:
    st.success(f"'{uploaded_file.name}' securely loaded into local memory.")
    st.markdown("---")
    st.subheader("Chat with your document")
    
    prompt = st.chat_input("Ask a question about the document...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown("*(Processing locally via Snapdragon NPU...)*")
            st.markdown(f"Based on the local analysis of {uploaded_file.name}, here is the information...")
