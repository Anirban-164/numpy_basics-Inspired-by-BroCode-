import numpy as np
"""
-> allows us to perform operations on arrays of different shapes and sizes
-> virtually expands dimensions of smaller array to match the shape of larger array without copying data

-> two arrays are compatible if
    1. their dimensions have same size
    2. one of their dimensions is 1
"""

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)  # (1, 4) = (a, b) [Let]
print(array2.shape)  # (4, 1) = (c, d) [Let]


"""
-> a != c but a = 1 --> OK
-> b != d but b = 1 --> OK
-> these two are compatible
"""
print(array1 * array2)
print(array1 + array2)
print(array1 - array2)
print(array1 / array2)

"""
HOW IT WORKS:
1. Start with the two shapes:
   - array1 has shape (1, 4) and values [[1, 2, 3, 4]]
   - array2 has shape (4, 1) and values [[1], [2], [3], [4]]

2. Broadcast them to a common (4, 4) grid:
   - array1 is repeated down 4 rows
   - array2 is repeated across 4 columns

   So they behave like this:

   array1:
   [[1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]]

   array2:
   [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

3. Multiply element by element:
   [[1*1, 2*1, 3*1, 4*1],
    [1*2, 2*2, 3*2, 4*2],
    [1*3, 2*3, 3*3, 4*3],
    [1*4, 2*4, 3*4, 4*4]]

   Result:
   [[ 1,  2,  3,  4],
    [ 2,  4,  6,  8],
    [ 3,  6,  9, 12],
    [ 4,  8, 12, 16]]

... For other operations
"""


array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(array3.shape)  # (3, 4) = (e, f) [Let]


"""
-> d != f but d = 1 --> OK
-> c != e --> NOT ok
-> these two are NOT compatible
"""
# print(array2 * array3) # will show error


"""
-> a != e but a = 1 --> OK
-> b = f --> OK
-> these two are compatible
"""
print(array1 * array3)
print(array1 + array3)
print(array1 - array3)
print(array1 / array3)

"""
WHAT HAPPENED THIS TIME?
-> array1 is [[1, 2, 3, 4]] --> shape (1, 4)

-> array3 is:
    [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
    --> shape (3, 4)

-> The second dimension already matches: 4 = 4
-> The first dimension is 1 in array1, so NumPy repeats that row 3 times to match array3

So array1 behaves like:
    [[1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]]
.
.
.
"""