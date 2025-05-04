def create_color_palette(palette_name, n_colors):
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Create a color palette
    palette = sns.color_palette(palette_name, n_colors)

    # Display the palette
    sns.palplot(palette)
    plt.title(f"{palette_name} Palette with {n_colors} Colors")
    plt.show()

def create_custom_palette(colors):
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Create a custom color palette
    palette = sns.color_palette(colors)

    # Display the custom palette
    sns.palplot(palette)
    plt.title("Custom Color Palette")
    plt.show()

def create_gradient_palette(start_color, end_color, n_colors):
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Create a gradient color palette
    palette = sns.light_palette(start_color, as_cmap=True, n_colors=n_colors)

    # Display the gradient palette
    sns.palplot(palette)
    plt.title(f"Gradient Palette from {start_color} to {end_color}")
    plt.show()