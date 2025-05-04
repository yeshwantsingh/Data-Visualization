import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
tips = sns.load_dataset("tips")

# Create a facet grid to display total bill amounts by day and time
g = sns.FacetGrid(tips, col="time", row="day", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total Bill", "Tip")
g.set_titles(col_template="{col_name}", row_template="{row_name}")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Facet Grid of Total Bill vs Tip by Day and Time")
plt.show()