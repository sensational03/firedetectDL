# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Conv2DTranspose, concatenate, Flatten, Dense, Dropout, Input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt

# def build_classification_model(input_shape=(256, 256, 3)):  # Change to 256x256
#     model = Sequential([
#         Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
#         MaxPooling2D(pool_size=(2, 2)),
#         Conv2D(64, (3, 3), activation='relu'),
#         MaxPooling2D(pool_size=(2, 2)),
#         Conv2D(128, (3, 3), activation='relu'),
#         MaxPooling2D(pool_size=(2, 2)),
#         Flatten(),
#         Dense(128, activation='relu'),
#         Dropout(0.5),
#         Dense(1, activation='sigmoid')
#     ])
#     model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#     return model

import keras
model = keras.Sequential()
model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(256,256,3)))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(64,(3,3),activation='relu'))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
model.add(keras.layers.MaxPool2D(2,2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
classification_model =model

def unet_model(input_size=(256, 256, 3)):  # Change to 256x256
    inputs = Input(input_size)
    
    # Encoding path
    c1 = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    c1 = Conv2D(32, (3, 3), activation='relu', padding='same')(c1)
    p1 = MaxPooling2D((2, 2))(c1)
    
    c2 = Conv2D(64, (3, 3), activation='relu', padding='same')(p1)
    c2 = Conv2D(64, (3, 3), activation='relu', padding='same')(c2)
    p2 = MaxPooling2D((2, 2))(c2)
    
    # Bottom layer
    c3 = Conv2D(128, (3, 3), activation='relu', padding='same')(p2)
    c3 = Conv2D(128, (3, 3), activation='relu', padding='same')(c3)
    
    # Decoding path
    u2 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c3)
    u2 = concatenate([u2, c2])
    c4 = Conv2D(64, (3, 3), activation='relu', padding='same')(u2)
    c4 = Conv2D(64, (3, 3), activation='relu', padding='same')(c4)
    
    u3 = Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c4)
    u3 = concatenate([u3, c1])
    c5 = Conv2D(32, (3, 3), activation='relu', padding='same')(u3)
    c5 = Conv2D(32, (3, 3), activation='relu', padding='same')(c5)
    
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(c5)
    model = Model(inputs=[inputs], outputs=[outputs])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

segmentation_model = unet_model()

# Classification Data Generators
classification_datagen = ImageDataGenerator(rescale=1.0/255.0,
                                            rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
train_classification_data = classification_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\classification\train",
    target_size=(256, 256),  # Change to 256x256
    class_mode='binary',
    batch_size=32
)
val_classification_data = classification_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\classification\val",
    target_size=(256, 256),  # Change to 256x256
    class_mode='binary',
    batch_size=32
)

# Segmentation Data Generators
segmentation_datagen = ImageDataGenerator(rescale=1.0/255.0)
train_segmentation_images = segmentation_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\train\images",
    target_size=(256, 256),  # Change to 256x256
    class_mode=None,
    batch_size=32,
    seed=42
)
train_segmentation_masks = segmentation_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\train\masks",
    target_size=(256, 256),  # Change to 256x256
    class_mode=None,
    batch_size=32,
    seed=42
)

val_segmentation_images = segmentation_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\val\images",
    target_size=(256, 256),  # Change to 256x256
    class_mode=None,
    batch_size=32,
    seed=42
)
val_segmentation_masks = segmentation_datagen.flow_from_directory(
    r"C:\Users\Anish\OneDrive\Desktop\Project I\segmentation\val\masks",
    target_size=(256, 256),  # Change to 256x256
    class_mode=None,
    batch_size=32,
    seed=42
)
classification_model.fit(
    train_classification_data,
    validation_data=val_classification_data,
    epochs=3
)
classification_model.save('classification_model_v1.keras')

# from tensorflow.image import rgb_to_grayscale

# def my_segmentation_generator(image_generator, mask_generator):
#     while True:
#         images = next(image_generator)  # use `next()` or `__next__()` to fetch the next batch
#         masks = next(mask_generator)  # use `next()` here as well
#         masks = rgb_to_grayscale(masks) 
#         yield images, masks




# # Create a custom generator for the segmentation data
# train_segmentation_data = my_segmentation_generator(train_segmentation_images, train_segmentation_masks)
# val_segmentation_data = my_segmentation_generator(val_segmentation_images, val_segmentation_masks)

# # Fit the model using the custom generators
# segmentation_model.fit(
#     train_segmentation_data,
#     validation_data=val_segmentation_data,
#     steps_per_epoch=len(train_segmentation_images),
#     validation_steps = len(val_segmentation_images),
#     epochs=10
# )


# segmentation_model.save('segmentation_model.keras')

"""
NOTES (AND ANALYSE)
UI
Try IP based segmentation over DL based segmentation (Otsu segmentation?)?
Shape, texture?
Video analytics?
PSPNet architecture?
Smoke class?
"""