
import numpy as np


def transform_vector(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """
    Apply a linear transformation to a vector.

    Args:
        matrix (np.ndarray): Transformation matrix.
        vector (np.ndarray): Input vector.

    Returns:
        np.ndarray: Transformed vector.

    Description:
        Applies a transformation matrix to an input vector
        and returns the resulting array.
    """
    result = matrix * vector
    return result


rotation_matrix = np.array([
    [0.0, -1.0],
    [1.0,  0.0]
])

vector = np.array([2.0, 3.0])

transformed_vector = transform_vector(rotation_matrix, vector)

print("Original vector:", vector)
print("Transformed vector:", transformed_vector)
