#import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import pdb 

# Line Plot (Daily Stock Prices)
#downloading data
# data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
# #creating a plot with specific size 
# plt.figure(figsize=(10, 6))
# #
# plt.plot(data.index, data['Close'])
# plt.title('AAPL Stock Prices')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.grid(True)
# pdb.set_trace()
# plt.show() 

# # Bar Plot (Iris Flower Dataset)
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# data = pd.read_csv(url, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# mean_sepal_length = data.groupby('class')['sepal_length'].mean()
# plt.figure(figsize=(10, 6))
# mean_sepal_length.plot(kind='bar')
# plt.title('Mean Sepal Length by Iris Class')
# plt.xlabel('Class')
# plt.ylabel('Mean Sepal Length')

# # Histogram (Titanic Passenger Survival Data)
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# data = pd.read_csv(url)
# plt.figure(figsize=(10, 6))
# plt.hist(data['Age'], bins=20)
# plt.title('Passenger Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')

# # Scatter Plot (Wine Quality Dataset)
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
# data = pd.read_csv(url, sep=';')
# plt.figure(figsize=(10, 6))
# plt.scatter(data['alcohol'], data['quality'])
# plt.title('Wine Quality vs. Alcohol Content')
# plt.xlabel('Alcohol Content')
# plt.ylabel('Quality')

# # Box Plot (Tips Dataset) 
#data = sns.load_dataset('tips')
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='day', y='total_bill', data=data)
# plt.title('Total Bill Amount by Day')

# Heatmap (Correlation Matrix of Iris Dataset)
# corr_matrix = data.corr()
# plt.figure(figsize=(10, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
# plt.title('Correlation Matrix of Iris Dataset')

data = sns.load_dataset('iris')
# Select only numeric columns
data = data.select_dtypes(include='number')
corr_matrix = data.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Iris Dataset')
plt.show()

# plt.show()
