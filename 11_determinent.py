import numpy as np 
# Define a square matrix 
matrix = np.array([ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9] 
]) 
# Calculate the determinant 
determinant = np.linalg.det(matrix) 
# Print the result 
print(f"Determinant of the matrix: {determinant:.2f}") 
# The np.linalg.det() function computes the determinant of the matrix.