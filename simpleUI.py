import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, messagebox

# Function to show Line Plot
def show_line_plot():
    # Line Plot (Daily Stock Prices)
    data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'])
    plt.title('AAPL Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

# Function to show Bar Plot
def show_bar_plot():
    # Bar Plot (Iris Flower Dataset)
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    data = pd.read_csv(url, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    mean_sepal_length = data.groupby('class')['sepal_length'].mean()
    plt.figure(figsize=(10, 6))
    mean_sepal_length.plot(kind='bar')
    plt.title('Mean Sepal Length by Iris Class')
    plt.xlabel('Class')
    plt.ylabel('Mean Sepal Length')
    plt.show()

# Function to show Histogram
def show_histogram():
    # Histogram (Titanic Passenger Survival Data)
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    data = pd.read_csv(url)
    plt.figure(figsize=(10, 6))
    plt.hist(data['Age'], bins=20)
    plt.title('Passenger Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# Function to show Scatter Plot
def show_scatter_plot():
    # Scatter Plot (Wine Quality Dataset)
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    data = pd.read_csv(url, sep=';')
    plt.figure(figsize=(10, 6))
    plt.scatter(data['alcohol'], data['quality'])
    plt.title('Wine Quality vs. Alcohol Content')
    plt.xlabel('Alcohol Content')
    plt.ylabel('Quality')
    plt.show()

# Function to show Box Plot
def show_box_plot():
    # Box Plot (Tips Dataset)
    data = sns.load_dataset('tips')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='day', y='total_bill', data=data)
    plt.title('Total Bill Amount by Day')
    plt.show()

def show_heatmap_iris():
    # Load Iris dataset
    data = sns.load_dataset('iris')
    
    # Select only numeric columns
    numeric_data = data.select_dtypes(include='number')
    
    # Calculate correlation matrix
    corr_matrix = numeric_data.corr()
    
    # Plot heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix of Iris Dataset')
    plt.show()

# Function to create pop-up window
def create_popup():
    root = Tk()
    root.title("Choose Plot Type")

    # Add buttons for each plot type
    line_button = Button(root, text="Line Plot", command=show_line_plot)
    line_button.pack()

    bar_button = Button(root, text="Bar Plot", command=show_bar_plot)
    bar_button.pack()

    hist_button = Button(root, text="Histogram", command=show_histogram)
    hist_button.pack()

    scatter_button = Button(root, text="Scatter Plot", command=show_scatter_plot)
    scatter_button.pack()

    box_button = Button(root, text="Box Plot", command=show_box_plot)
    box_button.pack()

    heatmap_button_iris = Button(root, text="Heatmap (Iris Dataset)", command=show_heatmap_iris)
    heatmap_button_iris.pack()

    root.mainloop()

# Create pop-up window
create_popup()
