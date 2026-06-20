import numpy as np


#scaler arythmatic
array = np.array([1, 2, 3, 4])

print (array + 2) #add 2 to each element
print (array - 2)
print (array * 2)
print (array / 2)
print (array ** 2) #raise each element to the power of 2


#vectorial math functions
print(np.pi) #value of pi
print(np.sqrt(array)) #square root of each element

new_array = np.array([1.01, 2.46, 3.5, 4.99])
print(np.floor(new_array))
print(np.ceil(new_array))
print(np.round(new_array))

print(np.pi * array ** 2) #area of circles with radius given by array elements


# element-wise arythmatic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2) #element-wise addition
print(array1 - array2) #element-wise subtraction
print(array1 * array2) #element-wise multiplication
print(array2 / array1) #element-wise division