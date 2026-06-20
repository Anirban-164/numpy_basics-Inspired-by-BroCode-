import numpy as np

my_list = [1, 2, 3, 4]
print (my_list)
my_list = my_list * 2
print (my_list)

my_array = np.array([1, 2, 3, 4])
print (my_array)
my_array = my_array * 2
print (my_array)


# 2d array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print('Dimensions of array:', array.ndim)
print(array)


# 3d array
new_array = np.array([[[1, 2, 3], [4, 5, 6]],
                      [[7, 8, 9], [10, 11, 12]]])
print('Dimensions of new_array:', new_array.ndim)
print('Shape of new_array (layer, row, column):', new_array.shape)
print(new_array)

# multidimensional array indexing
print(new_array[1][0][2])
print(new_array[1, 0, 2])


char_array = np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                       [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
                       [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', ' ']]])
word = char_array[0][2][1] + char_array[0][2][2]
print(word)