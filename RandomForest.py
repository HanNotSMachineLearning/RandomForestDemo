import csv
# Load random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.datasets import load_iris
iris = load_iris()

# Load Numpy
import numpy as np

np.random.seed(0)

available_diseases = ['Astma', 'Bronchitis', 'Griep', 'Longontsteking', 'Verkoudheid']
with open('Trainingsdata.csv', 'r') as DataFile:
    csv_file = list(csv.reader(DataFile))
    available_training_symptoms = list(
        map(lambda v: v.strip().lower(), csv_file[0]))[2:-1]
    trainData = csv_file[1:]

with open('Testdata.csv', 'r') as csvFile:
    csv_file = list(csv.reader(csvFile))
    available_test_symptoms = list(
        map(lambda v: v.strip().lower(), csv_file[0]))[2:-1]
    testData = csv_file[1:]

test_features = []
test_labels = []

train_features = []
train_labels = []

for item in trainData:
    train_labels.append(item[-1])
    train_features.append(item[:-1].copy())

for item in testData:
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())
clf = RandomForestClassifier(n_estimators=25, random_state=0)
clf.fit(train_features, train_labels)
pred = clf.predict(test_features)
print('Accuraatheid is: ' + str(metrics.accuracy_score(test_labels, pred)))
