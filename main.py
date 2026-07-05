import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

st.set_page_config(page_title="ATR Fix - Global AI Repair", layout="wide")

# Theme & Sidebar
st.sidebar.title("🌍 ATR Fix Global")
languages = {"English": "English", "Hindi": "Hindi", "Hinglish": "Hinglish", "Spanish": "Spanish"}
selected_lang = st.sidebar.selectbox("Select Language", list(languages.keys()))

# AI Engine
api_key = os.environ.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')

# Interface
st.title("🛠️ ATR Fix: What's Broken?")
img_file = st.file_uploader("Upload Problem Photo", type=['jpg', 'png', 'jpeg'])

if img_file:
    image = Image.open(img_file)
    st.image(image, use_column_width=True)
    if st.button("RUN DEEP ANALYSIS"):
        prompt = f"Identify the item and provide step-by-step repair instructions in {selected_lang}. Include safety warnings and tools needed."
        response = model.generate_content([prompt, image])
        st.markdown(response.text)
        
        # Voice Guide (Simple version for web)
        st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&q={response.text[:200]}&tl=en&client=tw-ob")
