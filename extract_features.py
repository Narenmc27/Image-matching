import numpy as np
from d2_net.feature_extraction import load_and_preprocess_image, extract_features
import os

# Directory containing the database images
database_dir = 'images/database/'

# List to store extracted features
database_features = []

# Loop through all images in the database directory
for image_filename in os.listdir(database_dir):
    image_path = os.path.join(database_dir, image_filename)
    try:
        image = load_and_preprocess_image(image_path)
        features = extract_features(image)
        database_features.append(features)
        print(f"Extracted features for {image_filename}")
    except Exception as e:
        print(f"Error processing {image_filename}: {e}")

# Save the extracted features to a .npy file
np.save('database_features.npy', np.array(database_features))
print(f"Features of {len(database_features)} images saved to 'database_features.npy'")
