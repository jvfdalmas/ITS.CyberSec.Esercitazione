#   Exercise 1
#   sklearn contains a "wine data set".

#     Find and load this data set
from sklearn.datasets import load_wine
data = load_wine()

#     Can you find a description?
print(data.DESCR)

#     What are the names of the classes?
print(data.target_names)

#     What are the features?
print(data.feature_names)

#     Where is the data and the labeled data?
#The copy of UCI ML Wine Data Set dataset is downloaded and modified to fit standard format from: https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
data = data.data
labelled_data = data.target



