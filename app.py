from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
 # .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("GOOGLE_API_KEY")

# API 키 설정
genai.configure(api_key=api_key)

st.set_page_config(page_title="Invoice Expert for SON",page_icon="🗣️")
st.header("Invoice Extracter Web Application for SON")
 
question = st.text_input("Write your question here...")
 
uploaded_image = st.file_uploader("Choose an Image..",type=["jpg","png","jpeg"])
 
image = ""
 
submit = st.button("Submit & Process")
 
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image,caption="Uploaded Image",use_column_width=True)
 
input_prompt = """You are an expert in understanding invoices, you will get the input
image as invoice and you will have to answer the question based on the input invoice.
If you get any other image then invoice, then reply with the following message.
```I understand invoices only, please upload a valid invoice and ask relevant questions
only```
"""
 
if submit:
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input_prompt,image,question])
    st.write(response.text)