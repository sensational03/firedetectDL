from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
classification_model = load_model(r"C:\Users\Anish\OneDrive\Desktop\Project I\classification_model_v1.keras")
segmentation_model = load_model(r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation_model.keras")

def detect_and_segment_fire(image):
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = tf.image.resize(image, (256, 256))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    print(img.shape)
    
    print(classification_model.predict(img))
    if classification_model.predict(img) < 0.19:
        img = tf.image.resize(image, (256, 256))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        mask = segmentation_model.predict(img)
        mask_rescaled = tf.image.resize(mask[0], image.shape[:2])
        res_img = mask_rescaled
        res_img = res_img.numpy() if isinstance(res_img, tf.Tensor) else res_img
        res_img = res_img.squeeze()
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(image)
        plt.title("Original Image")
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(res_img, cmap='gray')
        plt.title("Fire Segmentation Mask")
        plt.axis('off')
        plt.show()
    else:
        print("No fire detected in this image.")
        plt.imshow(image)

image_path = "nonfireme3.jpg"
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

detect_and_segment_fire(img)
