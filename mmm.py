import cv2
import matplotlib.pyplot as plt

# Load the noisy image from the specified path
image_path = r"C:\Users\arjun\Downloads\sam.jpg"
noisy_image = cv2.imread(image_path)

# Convert the image to grayscale (assuming it's a color image)
gray_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

# Apply the Non-Local Means (NLM) denoising algorithm
denoised_image = cv2.fastNlMeansDenoising(
    gray_image, None, h=10, searchWindowSize=21, templateWindowSize=7
)

# Display the original and denoised images using Matplotlib
plt.figure(figsize=(10, 5))

# Original Noisy Image
plt.subplot(121)
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title("Noisy Image")
plt.axis("off")

# Denoised Image
plt.subplot(122)
plt.imshow(denoised_image, cmap="gray")
plt.title("Denoised Image")
plt.axis("off")

plt.tight_layout()
plt.show()

import cv2
import matplotlib.pyplot as plt

# Load the noisy image from the specified path
image_path = r"C:\Users\arjun\Downloads\sam.jpg"
noisy_image = cv2.imread(image_path)

# Convert the image to grayscale (assuming it's a color image)
gray_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

# Apply the Non-Local Means (NLM) denoising algorithm
denoised_image = cv2.fastNlMeansDenoising(
    gray_image, None, h=10, searchWindowSize=21, templateWindowSize=7
)

# Display the original and denoised images using Matplotlib
plt.figure(figsize=(10, 5))

# Original Noisy Image
plt.subplot(121)
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title("Noisy Image")
plt.axis("off")

# Denoised Image
plt.subplot(122)
plt.imshow(denoised_image, cmap="gray")
plt.title("Denoised Image")
plt.axis("off")

plt.tight_layout()
plt.show()
