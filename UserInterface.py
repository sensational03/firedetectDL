import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

# Load both models with Keras
classification_model = tf.keras.models.load_model('classification_model_v1.keras')
segmentation_model = tf.keras.models.load_model('segmentation_model.keras')

# Function to preprocess the image for classification and segmentation
def preprocess_image(image, size=(256, 256)):
    image = image.resize(size)
    image = np.array(image) / 255.0
    if len(image.shape) == 2:  # For grayscale images
        image = np.stack((image,) * 3, axis=-1)  # Convert to 3 channels if grayscale
    return image

# Classification function
def classify_fire(image):
    input_image = np.expand_dims(image, axis=0)  # Add batch dimension
    predictions = classification_model.predict(input_image)
    return predictions[0][0] < 0.19  # Using 0.19 as the fire detection threshold

# Segmentation function
def segment_fire(image):
    input_image = np.expand_dims(image, axis=0)  # Add batch dimension
    mask = segmentation_model.predict(input_image)[0]  # Get first prediction from batch
    return mask

# Streamlit UI
st.title("Fire Detection and Segmentation")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    input_image = preprocess_image(image)

    # Step 1: Classification
    is_fire = classify_fire(input_image)

    if is_fire:
        st.write("Fire detected! Generating mask...")

        # Step 2: Segmentation
        mask = segment_fire(input_image)
        
        # Resize the mask to original image size and convert it to displayable format
        mask_resized = cv2.resize(mask, (image.width, image.height))
        mask_image = Image.fromarray((mask_resized * 255).astype(np.uint8))
        
        st.image(mask_image, caption="Fire Segmentation Mask", use_column_width=True)
    else:
        st.write("No fire detected.")

