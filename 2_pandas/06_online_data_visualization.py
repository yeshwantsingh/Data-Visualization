import pandas as pd
import matplotlib.pyplot as plt

# Load the Palmer Penguins dataset
penguins = pd.read_csv('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv')

# print(penguins.describe())

# print(penguins.head())

# # Create a histogram using Pandas plot
penguins['bill_length_mm'].plot.hist(bins=20, edgecolor='black', color='blue')

# Set plot labels and title
plt.xlabel('Bill Length (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Bill Length in Palmer Penguins')

# Show the plot
plt.show()

# print(penguins.head())
# print(penguins.filter(['island','bill_length_mm'])) # selecting columns
# penguins.filter(['island','bill_length_mm']).groupby('island')['bill_length_mm'].plot.kde() # group by on island
# # plot.kde()); # plotting the kde plot
# plt.legend() # adding legend
# plt.title('Distribution of bill length of penguins across islands') # add title
# plt.show() # show the plot


# Group by 'island' and 'sex', count the occurrences, and plot the result
# penguins_grouped = penguins.groupby(['island', 'sex']).size().unstack() # selecting columns groupby(['island', 'sex'])
# penguins_grouped.plot(kind='bar', stacked=True)
# plt.legend() # adding legend
# plt.title('Distribution of gender of penguins across islands') # add title
# plt.show() # show the plot


# students_attendance = pd.read_excel('pandas/attendance.xlsx')

# print(students_attendance.describe())
# print(students_attendance.head())


# students_attendance['Percentage'].plot.hist(bins=20, edgecolor='black', color='blue')

# plt.xlabel('Percentage')
# plt.ylabel('Frequency')
# plt.title('Histogram of Attendance Percentage')
# plt.show()
