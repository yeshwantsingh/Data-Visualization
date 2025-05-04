import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate some sample data
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Simple linear regression
sns.regplot(x=x, y=y, line_kws={"color": "red"})
plt.title("Simple Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.savefig("simple_linear_regression.png")
plt.show()

# Polynomial regression
from numpy.polynomial.polynomial import Polynomial

# Fit a polynomial of degree 2
p = Polynomial.fit(x, y, 2)
x_fit = np.linspace(0, 1, 100)
y_fit = p(x_fit)

plt.scatter(x, y, label='Data points')
plt.plot(x_fit, y_fit, color='green', label='Polynomial fit (degree 2)')
plt.title("Polynomial Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.savefig("polynomial_regression.png")
plt.show()

# Multiple regression example
import pandas as pd

# Create a DataFrame with multiple features
data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'target': 3 * np.random.rand(100) + 2 * np.random.rand(100) + np.random.normal(0, 0.5, 100)
})

# Fit a linear regression model
from sklearn.linear_model import LinearRegression

X = data[['feature1', 'feature2']]
y = data['target']
model = LinearRegression()
model.fit(X, y)

# Predict values
data['predicted'] = model.predict(X)

# Plotting the results
plt.scatter(data['feature1'], data['target'], color='blue', label='Actual')
plt.scatter(data['feature1'], data['predicted'], color='red', label='Predicted', alpha=0.5)
plt.title("Multiple Regression")
plt.xlabel("Feature 1")
plt.ylabel("Target")
plt.legend()
plt.grid()
plt.savefig("multiple_regression.png")
plt.show()