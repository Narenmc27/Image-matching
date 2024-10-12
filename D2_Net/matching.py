from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def match_images(query_features, database_features):
    """Finds the closest match for the query image from the database using Euclidean distance."""
    distances = euclidean_distances([query_features], database_features)
    closest_index = np.argmin(distances)
    return closest_index, distances[0][closest_index]
