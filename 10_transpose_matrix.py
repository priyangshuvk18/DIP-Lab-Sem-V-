# Define a matrix (list of lists) 
matrix = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9] 
] 
# Transpose the matrix 
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 
# Print the original and transposed matrices 
print("Original Matrix:") 
for row in matrix: 
    print(row) 
print("\nTransposed Matrix:") 
for row in transposed_matrix: 
    print(row) 