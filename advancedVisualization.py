import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import networkx as nx
from tkinter import Tk, Button

# Function to show 3D Surface Plot
def show_3d_surface_plot():
    # Generate data for 3D surface plot
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Plot 3D surface
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title('3D Surface Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Function to show Choropleth Map
def show_choropleth_map():
    # Generate data for choropleth map
    import geopandas as gpd
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Plot choropleth map
    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(column='pop_est', ax=ax, legend=True,
               legend_kwds={'label': "Population by Country",
                            'orientation': "horizontal"})
    ax.set_title('Choropleth Map')
    plt.show()

# Function to show Network Graph
def show_network_graph():
    # Generate data for network graph
    G = nx.karate_club_graph()

    # Plot network graph
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, edge_color='black', linewidths=1, font_size=10)
    plt.title('Network Graph')
    plt.show()

# Function to create pop-up window
def create_popup():
    root = Tk()
    root.title("Choose Plot Type")

    # Add buttons for each plot type
    surface_button = Button(root, text="3D Surface Plot", command=show_3d_surface_plot)
    surface_button.pack()

    choropleth_button = Button(root, text="Choropleth Map", command=show_choropleth_map)
    choropleth_button.pack()

    network_button = Button(root, text="Network Graph", command=show_network_graph)
    network_button.pack()

    root.mainloop()

# Create pop-up window
create_popup()
