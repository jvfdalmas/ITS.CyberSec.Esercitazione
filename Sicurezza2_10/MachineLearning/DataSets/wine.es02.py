#   Exercise 2
#   Create a scatter plot of the features ash and color_intensity of the wine data set.
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

data = load_wine()

features = 'ash', 'color_intensity'
features_index = [data.feature_names.index(features[0]),
                  data.feature_names.index(features[1])]

colors = ['blue', 'red', 'green']

for label, color in zip(range(len(data.target_names)), colors):
    plt.scatter(data.data[data.target==label, features_index[0]], 
                data.data[data.target==label, features_index[1]],
                label=data.target_names[label],
                c=color)

plt.xlabel(features[0])
plt.ylabel(features[1])
plt.legend(loc='upper left')
plt.show()