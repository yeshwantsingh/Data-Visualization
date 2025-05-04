import seaborn as sns
import matplotlib.pyplot as plt

# Example 1: Basic Strip Plot
def basic_strip_plot():
    tips = sns.load_dataset("tips")
    sns.stripplot(x="day", y="total_bill", data=tips)
    plt.title("Basic Strip Plot")
    plt.show()

# Example 2: Strip Plot with Jitter
def strip_plot_with_jitter():
    tips = sns.load_dataset("tips")
    sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
    plt.title("Strip Plot with Jitter")
    plt.show()

# Example 3: Strip Plot with Hue
def strip_plot_with_hue():
    tips = sns.load_dataset("tips")
    sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, dodge=True)
    plt.title("Strip Plot with Hue")
    plt.show()

# Example 4: Customizing Strip Plot
def customized_strip_plot():
    tips = sns.load_dataset("tips")
    sns.stripplot(x="day", y="total_bill", data=tips, palette="Set2", size=5)
    plt.title("Customized Strip Plot")
    plt.show()

if __name__ == "__main__":
    basic_strip_plot()
    strip_plot_with_jitter()
    strip_plot_with_hue()
    customized_strip_plot()