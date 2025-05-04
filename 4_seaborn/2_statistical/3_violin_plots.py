import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
tips = sns.load_dataset("tips")

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.show()

# Create a violin plot with hue
# plt.figure(figsize=(10, 6))
# sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
# plt.title("Violin Plot of Total Bill by Day and Gender")
# plt.xlabel("Day of the Week")
# plt.ylabel("Total Bill")
# plt.show()

# # Create a violin plot with inner boxplot
# plt.figure(figsize=(10, 6))
# sns.violinplot(x="day", y="total_bill", data=tips, inner="box")
# plt.title("Violin Plot of Total Bill by Day with Inner Boxplot")
# plt.xlabel("Day of the Week")
# plt.ylabel("Total Bill")
# plt.show()