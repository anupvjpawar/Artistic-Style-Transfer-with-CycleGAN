# Artistic Style Transfer with CycleGAN

This project showcases an artistic style transfer application using a pre-trained CycleGAN model. The app allows users to upload their images and see them transformed in the style of famous artworks. The user interface is built with Streamlit, and TensorFlow with TensorFlow Hub is used for style transfer.

## Project Structure


## Features

- **Image Upload:** Allows users to upload images in JPG, JPEG, or PNG format.
- **Style Transfer:** Applies artistic styles to uploaded images using a pre-trained CycleGAN model.
- **Result Display:** Shows both the original and stylized images side by side.

## Setup and Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/artistic_style_transfer.git
   cd artistic_style_transfer
   ```
2. Create a Virtual Environment

bash
```
python -m venv venv
```
```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
```
Install Dependencies
```

bash
```
pip install -r requirements.txt
```
Running the Application
Start the Streamlit App

bash
```
streamlit run app.py
```
Access the App

Open your web browser and navigate to http://localhost:8501.

