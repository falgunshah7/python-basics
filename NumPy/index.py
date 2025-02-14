import numpy as np

# Create a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
print("1D NumPy array:", arr)

# Create a 2D NumPy array
matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D NumPy array:\n", matrix2)

# array operations
print("Sum of array:", np.sum(arr))
print("Mean of array:", np.mean(arr))
print("Max of array:", np.max(arr))

# matrix operations
print("Transpose of matrix:\n", matrix2.T)
print("Matrix multiplication:\n", np.dot(matrix2, matrix2.T))

# Generating arrays
zeros_arr = np.zeros((3, 3))
print("Zeros array:\n", zeros_arr)
ones_arr = np.ones((2, 4))
print("Ones array:\n", ones_arr)
rand_arr = np.random.rand(3, 3)
print("Random array:\n", rand_arr)

# Reshaping arrays
# reshaped_arr = np.reshape(arr, (2, 3))
reshaped_arr1 = arr.reshape(2, 3)
print("Reshaped array1:\n", reshaped_arr1)
reshaped_arr2 = matrix2.reshape(3, 3)
print("Reshaped array2:\n", reshaped_arr2)

# Indexing and slicing
print("Element at index 2:", arr[2])
print("Element at index 0, 2:\n", matrix2[0, 2])
print("First row:\n", matrix2[0])
print("First column:\n", matrix2[:, 0])