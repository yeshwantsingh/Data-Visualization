import matplotlib.pyplot as plt

# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First subplot: Line plot
axs[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3], marker='o')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')

# Second subplot: Scatter plot
axs[0, 1].scatter([1, 2, 3, 4], [1, 4, 2, 3], color='r', marker='x')
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')

# Third subplot: Bar chart
axs[1, 0].bar(['A', 'B', 'C', 'D'], [3, 7, 5, 2])
axs[1, 0].set_title('Bar Chart')
axs[1, 0].set_xlabel('Categories')
axs[1, 0].set_ylabel('Values')

# Fourth subplot: Histogram
axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], bins=4, color='g', alpha=0.7)
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()