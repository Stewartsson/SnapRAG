import streamlit as st
from npu_engine import SnapdragonNPUManager

# Initialize the Snapdragon hardware manager
npu_manager = SnapdragonNPUManager()

st.set_page_config(page_title="SnapRAG - Local Enterprise AI", layout="centered")

st.title("⚡ SnapRAG: Zero-Trust Local AI")
st.markdown("Chat with confidential documents locally. **Powered by Snapdragon NPU.**")

uploaded_file = st.file_uploader("Upload a highly confidential PDF", type="pdf")

if uploaded_file is not None:
    st.success(f"'{uploaded_file.name}' securely loaded into local memory.")
    st.markdown("---")
    st.subheader("Document Chat")
    
    prompt = st.chat_input("Ask a question about the document...")
    if prompt:
        # Display user question
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Process and display AI response using the NPU Engine
        with st.chat_message("assistant"):
            st.markdown("*(Processing locally via Snapdragon NPU...)*")
            response = npu_manager.generate_local_response(prompt, uploaded_file.name)
            st.markdown(response)
