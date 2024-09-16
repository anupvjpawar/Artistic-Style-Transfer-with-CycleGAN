import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Load pre-trained CycleGAN model from TensorFlow Hub
def load_cycle_gan_model():
    model_url = 'https://tfhub.dev/google/cycle_gan/mosaic2photo/1'
    model = hub.load(model_url)
    return model

def load_image(image, img_size=(256, 256)):
    img = Image.open(image).resize(img_size)
    img = np.array(img) / 255.0
    return img[None, ...]

def preprocess_image(img):
    return tf.image.convert_image_dtype(img, dtype=tf.uint8)

def apply_style_transfer(model, content_img):
    stylized_img = model(content_img)
    return stylized_img
