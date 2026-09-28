# SnapRAG ⚡
**Zero-Trust On-Device Document Intelligence for Snapdragon-powered HP PCs.**

![Snapdragon Optimized](https://img.shields.io/badge/Optimized_for-Snapdragon_X_Elite-blue)
![Privacy](https://img.shields.io/badge/Privacy-100%25_Local-green)

## 📌 Overview
SnapRAG is a fully offline Retrieval-Augmented Generation (RAG) architecture. It allows enterprise users (legal, healthcare, finance) to query highly confidential PDFs without sending a single byte of data to a cloud server. 

## ⚙️ Qualcomm AI Hub & Hardware Integration
This project is explicitly architected to leverage the **Snapdragon Hexagon NPU**:
1. **LLM Engine:** Intended to deploy the quantized **Llama 3 (8B)** model provided by the Qualcomm AI Hub.
2. **Execution Provider:** Utilizes the Qualcomm Neural Network (QNN) API for hardware-accelerated inference, ensuring massive battery savings and low latency on HP Omnibook laptops.

## 📂 Project Structure
- `app.py`: The Streamlit-based frontend for seamless user interaction.
- `npu_engine.py`: The hardware orchestration layer connecting to the Snapdragon NPU.
- `requirements.txt`: Python environment dependencies.

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the local interface
```bash
streamlit run app.py
```
