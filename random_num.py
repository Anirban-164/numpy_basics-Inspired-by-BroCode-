import numpy as np

rng = np.random.default_rng()
# rng = np.random.default_rng(seed = 11) # --> seed is used to generate same random numbers every time the code is run

num = rng.integers(1, 100) # Generate a random integer between 1 and 99
print(num)

array = rng.integers(low=0, high=10, size=5) # Generate an array of 5 random integers between 0 and 9
print(array)

matrix = rng.integers(15, 50, size=(3, 4)) # Generate a 3x4 matrix of random integers between 15 and 50
print(matrix)

block = rng.integers(100, 200, size=(2, 3, 4)) # Generate a 2x3x4 block of random integers between 100 and 200
print(block)


fruits = np.array(['apple', 'banana', 'cherry', 'date', 'pineapple', 'grape', 'orange', 'kiwi', 'mango', 'pear'])

rng.shuffle(fruits) # Randomly shuffles the list of fruits
print(fruits)

random_fruit = rng.choice(fruits) # Randomly select a fruit from the list
print(random_fruit)

random_fruits = rng.choice(fruits, size=(2,3)) # Randomly select 3 unique fruits from the list
print(random_fruits)