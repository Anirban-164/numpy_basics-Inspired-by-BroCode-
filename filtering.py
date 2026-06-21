import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

seniors = ages[ages >= 65]
print(seniors)

adults = ages[ages >= 18]
print(adults)

teens = ages[(ages >= 13) & (ages < 18)]
print(teens)

evens = np.sort(ages[ages%2 == 0])
print(evens)

odds = np.where(ages%2 == 1, ages, 0)
print(odds)
# np.where(condition, value_if_true, value_if_false)
#   -> preserves the original shape of the array