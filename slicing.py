import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])


# row slicing
print(array[0])
print(array[1]) #2nd row
print(array[-1]) #last row
print(array[-4])

# array[start:end(exclusive):step]
print(array[1:3])  # Slicing a 2D array
print(array[:2])  # 1st two rows

print(array[::1]) # all rows by going 1 step
print(array[::-1]) # all rows by going 1 step backwards
print(array[::2])  # rows by going 2 steps (i.e. index 0, 2, 4, ...)
print(array[::-2]) # rows by going 2 steps backwards (i.e. index n-1, n-3, n-5, ...)


# column slicing
print(array[:, 0])  # 1st column
print (array[:, -2])  # 2nd column from last

print(array[:, 1:3])  # 2nd and 3rd columns
print(array[:, :2])  # 1st and 2nd columns
print(array[:, 1:])
print(array[:, ::2])  # 1st and 3rd columns
print(array[:, ::-1]) # 1st and 3rd columns from the end
print(array[:, ::-2]) # 1st and 3rd columns from the end by going 2 steps backwards

print(array[1:3, 1:3])  # 2nd and 3rd rows and columns
print(array[0:2, 2:4])
print(array[0:2:-1, 2:4:-1]) # will be empty because we are trying to slice from 0 to 2 by going backwards, which is not possible
print(array[1::-1, 3:1:-1]) # 1st and 2nd rows and 4th and 3rd columns by going backwards