from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 

iris = load_iris()

data, labels = iris.data, iris.target

res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=12)
train_data, test_data, train_labels, test_labels = res

knn = KNeighborsClassifier()
knn.fit(train_data, train_labels) 

predicted = knn.predict(test_data)
print("Predictions from the classifier:")
print(predicted)
print("Target values:")
print(test_labels)

accuracy = accuracy_score(predicted, test_labels)
print("Accuracy of the classifier:")
print(accuracy)
cf = confusion_matrix(test_labels, predicted)
print("Confusion matrix:")
print(cf)

# a complete check
predicted = knn.predict(data)
print("Predictions from the classifier:")
print(predicted)
print("Target values:")
print(labels)

accuracy = accuracy_score(labels, predicted)
print("Accuracy of the classifier:")
print(accuracy)
cf = confusion_matrix(labels, predicted)
print("Confusion matrix:")
print(cf)