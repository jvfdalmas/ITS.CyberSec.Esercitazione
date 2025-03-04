import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Print dataset information
print(iris["target_names"])
print(iris.target_names)
n_samples, n_features = iris.data.shape
print('Number of samples:', n_samples)
print('Number of features:', n_features)

# Print the first sample's measurements
print(iris.data[0])

# Create a histogram of petal width (feature index 3)
fig, ax = plt.subplots()
x_index = 3
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(iris.target_names)), colors):
    ax.hist(iris.data[iris.target==label, x_index], 
            label=iris.target_names[label],
            color=color)

# Set axis labels and legend
ax.set_xlabel(iris.feature_names[x_index])
ax.legend(loc='upper right')

# Create a scatter matrix
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
pd.plotting.scatter_matrix(iris_df,
                          c=iris.target,
                          figsize=(8, 8));

plt.show()