import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y)
plt.show() #the plot won't be displayed without this line


# marker modification
plt.plot(x, y,
        marker = ".",
        markersize = 20,
        markerfacecolor = "red",
        markeredgecolor = "black")
"""
Putting only 'color' will change the color of both the marker and the line
Other types of markers can be used as well: 
    1. "o" --> circle marker
    2. "s" --> square
    3. "D" --> diamond
    4. "v", "^", "<", ">" --> triangle down, up, left, right
    5. "p", "h" --> pentagon, hexagon
    6. "*", "+", "x"--> star, plus, cross
"""
plt.show()


# line modification
plt.plot(x, y,
        marker = 'o',
        markerfacecolor = "red",
        color = "blue",
        linewidth = 2,
        linestyle = "-.")
"""
other types of line styles can be used as well:
    1. "-" or 'solid'
    2. "--" or 'dashed'
    3. "-." or 'dash-dot'
    4. ":" or 'dotted'
"""
plt.show()


# multiple lines
line_style = dict(marker = 'o',
                markerfacecolor = "red",
                linewidth = 2,
                linestyle = "-.")
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

plt.plot(x, y, **line_style)
plt.plot(x, y2, **line_style, color = "black")
plt.plot(x, y3, **line_style, color = "green")
plt.show()


# labels
plt.title("Yearly Data",
          fontsize = 20,
          color = "blue",
          family = "Arial",
          fontweight = "bold")

plt.xlabel("Year", fontsize = 12, color = "black")
plt.ylabel("Value", fontsize = 12, color = "black")

plt.xticks(x) #shows year for only given values of x
y_ticks = sorted(set(np.concatenate((y, y2, y3))))
plt.yticks(y_ticks) #shows values for all three y arrays

plt.tick_params(axis = "both",
                labelsize = 10,
                color = "red", # modifies the color of the ticks
                labelcolor = "blue", # modifies the color of the labels beside the ticks
                direction = "inout", # direction of the ticks
                length = 10, # length of the ticks
                width = 2, # width of the ticks
)

plt.plot(x, y, **line_style)
plt.plot(x, y2, **line_style, color = "black")
plt.plot(x, y3, **line_style, color = "green")

plt.show()


# grid lines
plt.grid(axis = "both",
        color = "gray",
        linestyle = "--",
        linewidth = 1,
        alpha = 0.3) # transparency of the grid lines

plt.plot(x, y, **line_style)
plt.plot(x, y2, **line_style, color = "black")
plt.plot(x, y3, **line_style, color = "green")

plt.show()