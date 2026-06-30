import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['Grains', 'Fruits', 'Vegetables', 'Protein', 'Dairy', 'Sweets'])
values = np.array([4, 3, 2, 5, 3, 7])

# bar-chart
plt.bar(categories, values, color = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0'])
# plt.barh(categories, values) # horizontal bar chart

plt.title("Daily Food Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()


# pie-chart
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0']
explodes = (0.1, 0, 0, 0, 0, 0) # to move a slice away from the center of the pie chart
plt.pie(values,
        labels = categories,
        autopct = '%1.2f%%', # auto percentage
        startangle = 90,
        colors = colors,
        explode = explodes,
        shadow = True, # adds shadow to the pie chart,
        counterclock = False # to rotate the pie chart in counter-clockwise direction
        )

plt.title("Daily Food Consumption")
plt.show()