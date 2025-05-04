import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create a swarm plot
plt.figure(figsize=(10, 6))
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.title("Swarm Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.show()