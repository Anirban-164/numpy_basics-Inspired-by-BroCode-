import matplotlib.pyplot as plt
import numpy as np

# scatter plot (only dots)
x = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])

plt.scatter(x, y,
            color = "blue",
            s = 50) # s is the size of the marker

x2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y2 = np.array([50, 55, 60, 58, 63, 65, 70, 72, 75, 78, 80])

plt.scatter(x2, y2,
            color = "red",
            s = 50) # s is the size of the marker

plt.title("Test scores")
plt.xlabel("Hours studies")
plt.ylabel("Grades")

plt.show()


# histogram
scores = np.random.normal(loc = 80, scale = 10, size = 100) # loc = the mean, scale = standard deviation
scores = np.clip(scores, 0, 100) # to limit the values between 0 and 100

plt.hist(scores)
plt.title("Test scores")

plt.hist(scores,
         bins = 10,
         color = "green",
         edgecolor = "black") # bins = number of bars in the histogram

plt.show()


# subplots
x = np.array([0, 1, 2, 3, 4, 5])

figure, axes = plt.subplots(nrows = 3, ncols = 2)

axes[0, 0].plot(x, x*2, color = "blue") # y = 2x
axes[0, 0].set_title("y = 2x")

axes[0, 1].plot(x, x**2, color = "red") # y = x^2
axes[0, 1].set_title("y = x^2")

axes[1, 0].bar(x, x**3, color = "blue") # y = x^3
axes[1, 0].set_title("y = x^3")

axes[1, 1].plot(x, x**0.5, color = "blue") # y = sqrt(x)
axes[1, 1].set_title("y = sqrt(x)")

axes[2, 0].plot(x, np.log(x + 1), color = "blue") # y = log(x)
axes[2, 0].set_title("y = log(x)")

axes[2, 1].plot(x, np.exp(x), color = "blue")
axes[2, 1].set_title("y = exp(x)")

plt.tight_layout() # to avoid overlapping of the subplots
plt.show()