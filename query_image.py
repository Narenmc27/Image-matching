import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import time
from d2_net.feature_extraction import load_and_preprocess_image, extract_features
from d2_net.matching import match_images

# Start measuring time
start_time = time.time()

# Path to query image
query_image_path = r"Z:\Naren's\Intern@FOVIA TECH\Project\Failure\images\query\query_image.jpg"

# Path to the database directory containing the images
database_dir = 'images/database/'

# Load the query image and preprocess it
query_image = load_and_preprocess_image(query_image_path)

# Extract features from the query image
query_features = extract_features(query_image)

# Load the features of the image database
database_features = np.load('database_features.npy', allow_pickle=True)

# Match query image with the database
closest_index, distance = match_images(query_features, np.array(database_features))

# Get the list of filenames in the database directory
database_images = os.listdir(database_dir)

# Map the closest index to the corresponding filename
closest_image_filename = database_images[closest_index]

# End measuring time
end_time = time.time()

# Calculate the total time taken
time_taken = end_time - start_time

# Print the closest match, distance, and time taken
print(f"Closest match found at index {closest_index} with distance {distance}")
print(f"Closest match image: {closest_image_filename}")
print(f"Time taken: {time_taken:.2f} seconds")

# Load the closest match image
closest_image_path = os.path.join(database_dir, closest_image_filename)
closest_image = cv2.imread(closest_image_path)

# Convert the closest image to RGB for matplotlib display
closest_image_rgb = cv2.cvtColor(closest_image, cv2.COLOR_BGR2RGB)

# Load the query image for display (convert to RGB)
query_image_rgb = cv2.cvtColor(cv2.imread(query_image_path), cv2.COLOR_BGR2RGB)

# Plot both images side by side for comparison
plt.subplot(1, 2, 1)
plt.imshow(query_image_rgb)
plt.title('Query Image')

plt.subplot(1, 2, 2)
plt.imshow(closest_image_rgb)
plt.title(f'Closest Match (Index: {closest_index})')

# Show the images
plt.show()
