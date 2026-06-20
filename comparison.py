import numpy as np

# comparison operators
scores = np.array([85, 90, 80, 78, 92, 88])
print(scores > 90)
print(scores <= 80)
print(scores == 88)

scores[scores % 3 == 0] = 100
print(scores)