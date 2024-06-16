import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import preprocess_input

# Load the VGG16 model with pre-trained weights (you can change the weights argument)
model = VGG16(
    weights="imagenet", include_top=False
)  # Exclude the top classification layer


# Define a function to extract features from an image
def extract_features(image_path):
    img = load_img(
        image_path, target_size=(224, 224)
    )  # VGG16 requires input size 224x224
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess the image for VGG16

    # Get feature representation from the last convolutional layer
    features = model.predict(img_array)

    return features


# Example usage
image_path = "C:\\Users\\arjun\\Desktop\\dataset\\class1\\sam.jpg"
# Replace with the path to your image
image_features = extract_features(image_path)
print(image_features.shape)  # This will show the shape of the extracted features
