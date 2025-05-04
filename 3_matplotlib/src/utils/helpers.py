def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def save_plot(figure, filename):
    figure.savefig(filename)

def show_plot(figure):
    import matplotlib.pyplot as plt
    plt.show()

def set_plot_style(style='seaborn'):
    import matplotlib.pyplot as plt
    plt.style.use(style)

def create_color_map(num_colors):
    import matplotlib.cm as cm
    return [cm.viridis(i) for i in range(num_colors)]