import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from styles.style_transfer import load_cycle_gan_model, load_image, apply_style_transfer, preprocess_image

# Load the CycleGAN model
model = load_cycle_gan_model()

# Streamlit app
st.title("Artistic Style Transfer with CycleGAN")

st.sidebar.header("Upload your image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.sidebar.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Load and process the image
    content_img = load_image(uploaded_file)
    
    # Apply style transfer
    stylized_img = apply_style_transfer(model, content_img)

    # Convert images to display
    content_img_display = preprocess_image(content_img)
    stylized_img_display = preprocess_image(stylized_img)

    # Display the results
    st.image(content_img_display[0], caption='Content Image', use_column_width=True)
    st.image(stylized_img_display[0], caption='Stylized Image', use_column_width=True)
