import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, Button

import pdb

# Function to show Cooler Heatmap with Weather Data
def show_cooler_heatmap():
    # Load flights dataset from Seaborn
    data = sns.load_dataset("flights")
    #pdb.set_trace() 
    # Pivot the DataFrame to create a heatmap
    #data = flights_data.pivot("month", "year", "passengers")
    
    # Plot heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, cmap='coolwarm', annot=True, fmt="d", linewidths=0.5)
    plt.title('Passenger Counts by Month and Year')
    plt.xlabel('Year')
    plt.ylabel('Month')
    plt.show()

# Function to create pop-up window
def create_popup():
    root = Tk()
    root.title("Choose Plot Type")

    # Add buttons for each plot type
    heatmap_button_cooler = Button(root, text="Cooler Heatmap (Flights Data)", command=show_cooler_heatmap)
    heatmap_button_cooler.pack()

    root.mainloop()

# Create pop-up window
create_popup()
