import matplotlib.pyplot as plt
import numpy as np
import scipy
from datetime import datetime, timedelta
from random import randint
from sklearn.preprocessing import normalize


def generate_matrix(rows, cols):
    return np.random.randint(100, size=(rows, cols))
    # return np.reshape([randint(0, 100) for _ in range(rows * cols)], (rows, cols))


# 1. Create a vector with values ranging from 10 to 49. Reverse a vector (first element becomes last)
# vector = np.arange(10, 50)
# reversedVector = np.flip(vector)
# print(vector)
# print(reversedVector)

# 2. Create a 5x5 array with random values and find the minimum and maximum values
# matrix = generate_matrix(5, 5)
# print(np.array(matrix))
# print("min: %d max: %d" % (matrix.min(), matrix.max()))

# 3. Normalize a 5x5 random matrix
# matrix = generate_matrix(5, 5)
# normalized = normalize(matrix, axis=1, norm='l1')  # normalized by row
# print(np.array(matrix))
# print(np.array(normalized))

# 4. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
# matrix_a = generate_matrix(5, 3)
# matrix_b = generate_matrix(3, 2)
# product = np.dot(matrix_a, matrix_b)
# print(np.array(product))

# 5. How to get the dates of yesterday, today and tomorrow?
# yesterday = datetime.now() - timedelta(1)
# today = datetime.now()
# tomorrow = datetime.now() + timedelta(1)
# print(yesterday.strftime('%Y-%m-%d'))
# print(today.strftime('%Y-%m-%d'))
# print(tomorrow.strftime('%Y-%m-%d'))

# 6. Extract the integer part of a random array using 5 different methods
# matrix = np.random.uniform(0, 100, 5)
# print("Original", matrix)
# print(matrix - matrix % 1)
# print(np.floor(matrix))
# print(np.ceil(matrix) - 1)
# print(matrix.astype(int))
# print(np.trunc(matrix))

# plot pie chart
# fig1, ax1 = plt.subplots()
# ax1.pie(matrix.astype(int), labels=range(5), autopct='%1i%%')
# ax1.axis('equal')
# plt.show()

# 7. Create a structured array representing a position (x,y) and a color (r,g,b)
# structured_array = np.array([
#     ((12, 13), (0, 0, 255)),
#     ((102, 16), (128, 128, 0)),
# ], dtype='2i, 3i')
# print(structured_array)

# 1. Consider a generator function that generates 10 integers and use it to build an array
def int_generator():
    for i in range(10):
        yield randint(0, 100)


output = np.fromiter(int_generator(), dtype=int, count=-1)
print(output)

fig, ax = plt.subplots()
ax.bar(range(10), output)
ax.set_title('10 Integers from a Generator Function')
plt.show()

# 2. Consider two random array A and B, check if they are equal
# rand_a = np.random.rand(6)
# rand_b = np.random.rand(6)
# print(np.array_equal(rand_a, rand_b))

# 3. Consider a random vector with shape (100,2) representing coordinates, find point by point distances
# matrix = np.random.random((100, 2))
# result = scipy.spatial.distance.cdist(matrix, matrix)
# print(result)

# 4. Subtract the mean of each row of a matrix
# matrix = generate_matrix(5, 5)
# result = matrix - matrix.mean(axis=1, keepdims=True)
# print(matrix)
# print(result)

# 5. How to I sort an array by the nth column?
# matrix = generate_matrix(4, 4)
# sort_column = 3
# result = matrix[matrix[:, sort_column].argsort()]
# print(matrix)
# print(result)

# 6. Compute a matrix rank
# matrix = generate_matrix(5, 5)
# rank = np.linalg.matrix_rank(matrix)
# print(rank)

# 7. Consider a 16x16 array, how to get the block-sum (block size is 4x4)
# matrix = np.ones((16, 16))
# block = 4
# result = np.add.reduceat(
#     np.add.reduceat(matrix, np.arange(0, matrix.shape[0], block), axis=0),
#     np.arange(0, matrix.shape[1], block),
#     axis=1
# )
# print(result)
