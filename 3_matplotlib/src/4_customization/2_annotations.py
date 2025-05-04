import matplotlib.pyplot as plt

# Example 1: Basic Annotation
def basic_annotation():
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9], label='Quadratic Growth')
    plt.title('Basic Annotation Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.annotate('Peak', xy=(2, 4), xytext=(2, 5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

# Example 2: Multiple Annotations
def multiple_annotations():
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y, marker='o')
    plt.title('Multiple Annotations Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    for i in range(len(x)):
        plt.annotate(f'({x[i]}, {y[i]})', xy=(x[i], y[i]), 
                     xytext=(x[i], y[i] + 1),
                     arrowprops=dict(facecolor='red', arrowstyle='->'))
    
    plt.show()

# Example 3: Annotation with a Box
def annotation_with_box():
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9], label='Quadratic Growth')
    plt.title('Annotation with Box Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.annotate('Important Point', xy=(2, 4), xytext=(3, 5),
                 bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightyellow'),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.show()

# Example 4: Annotation with Different Fonts
def annotation_with_fonts():
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9], label='Quadratic Growth')
    plt.title('Annotation with Different Fonts Example')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.annotate('Stylish Annotation', xy=(2, 4), xytext=(1, 5),
                 fontsize=12, fontweight='bold', color='blue',
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.show()

if __name__ == "__main__":
    basic_annotation()
    multiple_annotations()
    annotation_with_box()
    annotation_with_fonts()