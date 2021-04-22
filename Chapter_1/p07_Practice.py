""" Rotating a Matrix """
# In a pythonic way
def rotating_matrix_pythonic(matrix):
    n = len(matrix)
    result = [[0] * n for i in range(n)] 
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result

print(rotating_matrix_pythonic([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))