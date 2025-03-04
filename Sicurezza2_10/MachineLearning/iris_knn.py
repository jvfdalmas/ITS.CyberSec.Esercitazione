from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix 

#  per caricare il dataset Iris
iris = load_iris()

# per dividere i dati in set di addestramento e test
# data contiene le caratteristiche dei fiori (lunghezza e larghezza di sepali e petali) e labels contiene le etichette delle specie (0, 1, 2)
data, labels = iris.data, iris.target

# I dati vengono divisi in modo che l'80% venga utilizzato per l'addestramento e il 20% per il test. random_state=12 garantisce che la divisione sia riproducibile.
res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=12)
train_data, test_data, train_labels, test_labels = res

# Viene creato un classificatore KNN con i parametri predefiniti e addestrato sui dati di training.
knn = KNeighborsClassifier() 
knn.fit(train_data, train_labels) 

# Sono i valori che il modello KNN ha previsto dentro TEST
predicted = knn.predict(test_data)
print("Predictions from the classifier:")
print(predicted)
# Sono i valori reali o le etichette vere del dataset
print("Target values:")
print(test_labels)

#  misura la percentuale di previsioni corrette dentro TEST
accuracy = accuracy_score(predicted, test_labels)
print("Accuracy of the classifier:")
print(accuracy)

# mostra in dettaglio quali classi sono state confuse tra loro dentro TEST
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