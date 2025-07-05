# GenAI Resume Screener

This is a simple Generative AI-powered resume screener built with Streamlit.

## Features
- Upload resumes in `.txt` format
- Automatically summarize using a Transformer summarizer (BART/T5)
- View candidate insights instantly

## Setup
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Model Used
HuggingFace summarization pipeline (e.g., facebook/bart-large-cnn)