import streamlit as st
import requests
from PIL import Image
import io

# API Endpoint (replace with your deployed API URL)
API_URL = "https://api-deploy-cnt1.onrender.com/predict/"

# Page title & styling
st.set_page_config(page_title="Cat vs. Dog Classifier", page_icon="🐶", layout="centered")
st.title("🐶 Cat vs. Dog Classifier 🐱")
st.markdown("### Upload an image and let AI classify it!")

# Sidebar
st.sidebar.markdown("## Instructions:")
st.sidebar.write("1️⃣ Upload a **JPG/PNG** image.\n\n2️⃣ Click **Predict** to get classification.")

# File uploader
uploaded_file = st.file_uploader("📂 Choose an image...", type=["jpg", "png", "jpeg"])

# Display image and add Predict button
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)
    
    if st.button("🔍 Predict"):
        # Convert image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="JPEG")
        img_bytes = img_bytes.getvalue()

        # API request
        with st.spinner("Let me classify"):
            response = requests.post(API_URL, files={"file": img_bytes})

            if response.status_code == 200:
                result = response.json()
                st.success(f" **my Prediction is :** {result['prediction']} ")
            else:
                st.error("❌ Error: Unable to get prediction. Please try again.")
