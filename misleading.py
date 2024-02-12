import matplotlib.pyplot as plt
from tkinter import Tk, Button

# Function to show misleading bar plot
def show_misleading_bar_plot():
    # Data for bar plot
    categories = ['Category A', 'Category B', 'Category C']
    values = [100, 105, 110]  # Adjusted values to range from 100 to 102

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values)
    plt.ylim(100, 110)  # Set y-axis range from 100 to 110
    plt.title('Misleading Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

# Function to create pop-up window
def create_popup():
    root = Tk()
    root.title("Choose Plot Type")

    # Add buttons for each misleading plot type
    bar_button = Button(root, text="Misleading Bar Plot", command=show_misleading_bar_plot)
    bar_button.pack()

    root.mainloop()

# Create pop-up window
create_popup()
