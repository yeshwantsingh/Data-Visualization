import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode the 1st slice

# Basic pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Basic Pie Chart Example')
plt.show()

# Pie chart with custom colors and no shadow
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Pie Chart without Shadow')
plt.show()

# Pie chart with percentage labels only
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=None, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Pie Chart with Percentage Labels Only')
plt.show()