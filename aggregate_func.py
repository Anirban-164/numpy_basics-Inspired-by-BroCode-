import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array)) # sum of all elements
print(np.sum(array[0])) # sum of first row
print(np.sum(array, axis=0)) # sum of each column
print(np.sum(array, axis=1)) # sum of each row

print(np.mean(array)) # avg of all elements
print(np.mean(array[0])) # avg of first row
print(np.mean(array, axis=0)) # avg of each column
print(np.mean(array, axis=1)) # avg of each row

print(np.min(array)) # min of all elements
print(np.max(array)) # max of all elements
print(np.argmin(array)) # index of min element (flattened)
print(np.argmax(array)) # index of max element (flattened)

# Use unravel_index to get the index in 2D format
min_idx = np.unravel_index(np.argmin(array), array.shape) # stores tuple of indices
max_idx = np.unravel_index(np.argmax(array), array.shape)
print(tuple(map(int, min_idx))) # convert to standard integer tuple
print(tuple(map(int, max_idx)))

print(np.median(array)) # median of all elements
print(np.std(array)) # standard deviation
print(np.var(array)) # variance