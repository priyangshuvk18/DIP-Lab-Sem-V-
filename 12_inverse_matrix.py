import numpy as np 
# Define a square matrix 
matrix = np.array([ 
[4, 7], 
[2, 6] 
]) 
# Check if the determinant is non-zero 
determinant = np.linalg.det(matrix) 
if determinant != 0: 
# Calculate the inverse 
    inverse_matrix = np.linalg.inv(matrix) 
    print(inverse_matrix) 
else: 
    print("The matrix is singular and does not have an inverse.") 