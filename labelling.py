import cv2
import os

# Define the path to your dataset directory
dataset_dir = "C:\\Users\\arjun\\Desktop\\dataset"


# Create a list of image file names in the dataset directory
image_files = os.listdir(dataset_dir)

# Initialize variables for labeling
current_index = 0
total_images = len(image_files)
labels = []

# Create a window for labeling
cv2.namedWindow("Image Labeling")

while current_index < total_images:
    # Load the current image
    image_file = os.path.join(dataset_dir, image_files[current_index])
    image = cv2.imread(image_file)

    # Display the image
    cv2.imshow("Image Labeling", image)

    # Wait for user input
    key = cv2.waitKey(0)

    # Label the image
    if key == ord("r"):  # Press 'r' for real (authentic) image
        labels.append("real")
    elif key == ord("f"):  # Press 'f' for fake (manipulated) image
        labels.append("fake")
    elif key == ord("n"):  # Press 'n' to skip to the next image without labeling
        labels.append("skip")

    current_index += 1

# Close the labeling window
cv2.destroyAllWindows()

# Save the labels to a text file
with open("labels.txt", "w") as label_file:
    for i, label in enumerate(labels):
        label_file.write(f"{image_files[i]}: {label}\n")

print("Labeling completed. Labels saved to 'labels.txt'.")
