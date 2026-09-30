import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])


# row slicing
print('-----------row slicing-----------')
print(array[0])
print(array[1]) #2nd row
print(array[-1]) #last row
print(array[-4]) # 4th row from the last

# array[start:end(exclusive):step]
print(array[1:3])  # Slicing a 2D array --> row 1-2
print(array[:2])  # 1st two rows

print(array[::1]) # all rows by going 1 step
print(array[::-1]) # all rows by going 1 step backwards --> row 4, row 3, row 2, row 1
print(array[::2])  # rows by going 2 steps (i.e. index 0, 2, 4, ...)
print(array[::-2]) # rows by going 2 steps backwards (i.e. index n-1, n-3, n-5, ...)


# column slicing
print('-----------column slicing-----------')
print(array[:, 0])  # 1st column
print (array[:, -2])  # 2nd column from last

print(array[:, 1:3])  # 2nd and 3rd columns --> column 1, column 2
print(array[:, :2])  # 1st and 2nd columns
print(array[:, 1:])
print(array[:, ::2])  # 1st and 3rd columns
print(array[:, ::-1]) # 1st and 3rd columns from the end
print(array[:, ::-2]) # 1st and 3rd columns from the end by going 2 steps backwards

# row and column slicing
print('-----------row and column slicing simultaneously-----------')
print(array[1:3, 1:3])  # 2nd and 3rd rows and columns
print(array[0:2, 2:4])
print(array[:2, 2:]) #same as previous line
print(array[0:2:-1, 2:4:-1]) # will be empty because we are trying to slice from 0 to 2 by going backwards, which is not possible
print(array[1::-1, 3:1:-1]) # 1st and 2nd rows and 4th and 3rd columns by going backwards