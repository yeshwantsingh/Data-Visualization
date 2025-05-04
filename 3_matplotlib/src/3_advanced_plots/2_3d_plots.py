import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Example 1: Basic 3D Scatter Plot
def basic_3d_scatter():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = np.random.rand(100)
    
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_title('Basic 3D Scatter Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    plt.show()

# Example 2: 3D Line Plot
def basic_3d_line():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    z = np.linspace(0, 1, 100)
    x = z * np.sin(25 * z)
    y = z * np.cos(25 * z)
    
    ax.plot(x, y, z)
    ax.set_title('3D Line Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    plt.show()

# Example 3: 3D Surface Plot
def basic_3d_surface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title('3D Surface Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    plt.show()

# Example 4: 3D Wireframe Plot
def basic_3d_wireframe():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    
    ax.plot_wireframe(x, y, z, color='black')
    ax.set_title('3D Wireframe Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    plt.show()

if __name__ == "__main__":
    basic_3d_scatter()
    basic_3d_line()
    basic_3d_surface()
    basic_3d_wireframe()