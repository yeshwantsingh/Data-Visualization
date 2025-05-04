import matplotlib.pyplot as plt
import geopandas as gpd

def plot_geographic_data():
    # Load geographic data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Create a basic plot
    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(ax=ax, color='lightblue', edgecolor='black')

    # Set title and labels
    ax.set_title('Geographic Plot of World Countries', fontsize=15)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)

    # Show the plot
    plt.show()

def plot_geographic_data_with_population():
    # Load geographic data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Create a basic plot with population data
    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(column='pop_est', ax=ax, legend=True,
               legend_kwds={'label': "Population by Country",
                            'orientation': "horizontal"},
               cmap='OrRd')

    # Set title and labels
    ax.set_title('Geographic Plot of World Countries by Population', fontsize=15)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_geographic_data()
    plot_geographic_data_with_population()