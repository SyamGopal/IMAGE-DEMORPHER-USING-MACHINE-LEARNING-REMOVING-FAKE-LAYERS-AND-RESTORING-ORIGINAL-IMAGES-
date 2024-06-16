import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define the image dimensions and batch size
img_height = 224  # Adjust as needed
img_width = 224  # Adjust as needed
batch_size = 32  # Adjust as needed

# Define the path to your dataset (with separate folders for each class)
data_dir = r"C:\Users\arjun\Desktop\dataset"


# Data Preprocessing
datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,  # Normalize pixel values to [0, 1]
    rotation_range=20,  # Randomly rotate images by up to 20 degrees
    width_shift_range=0.2,  # Randomly shift images horizontally by up to 20% of the width
    height_shift_range=0.2,  # Randomly shift images vertically by up to 20% of the height
    shear_range=0.2,  # Shear transformations
    zoom_range=0.2,  # Randomly zoom in on images
    horizontal_flip=True,  # Randomly flip images horizontally
    fill_mode="nearest",  # Fill in missing pixels using the nearest-neighbor method
)

# Create a generator for the dataset
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="binary",  # Set this to 'categorical' if you have multiple classes
)

# Optionally, you can print class labels and class indices
# Print class labels and class indices
print("Class labels:", train_generator.class_indices)

print("Class indices:", train_generator.class_indices)
