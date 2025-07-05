import streamlit as st
from transformers import pipeline

st.title("GenAI Resume Screener")
st.write("Upload a resume and get key candidate insights.")

summarizer = pipeline("summarization")
uploaded_file = st.file_uploader("Upload Resume (Text format)", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    if len(text) > 100:
        summary = summarizer(text[:1000], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        st.subheader("Candidate Summary:")
        st.write(summary)
    else:
        st.warning("Resume content too short to summarize.")