import streamlit as st
import os
from app.firebase_admin_setup import storage
from datetime import datetime

st.set_page_config(page_title="Refined x Reassured", layout="centered")

st.title("💎 Refined x Reassured – Upload for Estimate")

st.markdown("Upload **4 walk-up videos** (front, back, left, right). Start from 50 ft away and walk slowly toward the house.")

uploaded_files = st.file_uploader(
    "Upload your walk-up videos here:",
    type=["mp4", "mov", "avi"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.video(file)

    if st.button("Submit to Sky AI"):
        st.success("🎉 Videos submitted for review! You’ll get your estimate shortly.")
