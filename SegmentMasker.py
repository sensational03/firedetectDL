import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def create_fire_mask(image):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_bound1 = np.array([0, 120, 150])
    upper_bound1 = np.array([25, 255, 255])
    mask1 = cv2.inRange(hsv_image, lower_bound1, upper_bound1)

    lower_bound2 = np.array([18, 100, 180])
    upper_bound2 = np.array([35, 255, 255])
    mask2 = cv2.inRange(hsv_image, lower_bound2, upper_bound2)
    

    mask = cv2.bitwise_or(mask1, mask2)
    

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return mask

def process_images(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)
    

    for filename in os.listdir(input_folder):

        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):

            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            mask = create_fire_mask(image)

            mask_filename = f"mask_{filename}"
            mask_path = os.path.join(output_folder, mask_filename)
            cv2.imwrite(mask_path, mask)


input_folder = r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\val\images\non_fire"
output_folder = r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\val\masks\non_fire"

process_images(input_folder, output_folder)
