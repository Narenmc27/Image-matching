import torch
import torchvision.models as models
import torchvision.transforms as transforms
import cv2
import numpy as np

# Load the pre-trained ResNet model
model = models.resnet50(weights='IMAGENET1K_V1')
model.eval()  # Set the model to evaluation mode

# Preprocessing for images (resizing and normalizing to match ResNet's input)
preprocess = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_and_preprocess_image(image_path):
    """Loads an image and preprocesses it for ResNet."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be loaded.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = preprocess(image)  # Apply the preprocessing
    return image

def extract_features(image):
    """Extracts features from an image using ResNet-50."""
    image = image.unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        features = model(image)  # Pass image through the model
    return features.numpy().flatten()  # Return flattened feature vector
