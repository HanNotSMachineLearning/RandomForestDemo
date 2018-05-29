import csv
# Load random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# Load Numpy
import numpy as np

np.random.seed(0)

amount_trees = 25

# Lijst van beschikbare ziekten
available_diseases = ['Astma', 'Bronchitis', 'Griep', 'Longontsteking', 'Verkoudheid']
datasize = None
while datasize is None:
    print("\nKies een dataset: 25, 50, 75 of 100:")
    datasize = input("")

#Uitlezen van bestand en filteren van data
with open('Data/Dataset-'+datasize+'.csv', 'r') as DataFile:
    csv_file = list(csv.reader(DataFile))
    available_training_symptoms = list(
        map(lambda v: v.strip().lower(), csv_file[0]))[2:-1]
    trainData = csv_file[1:]

# Uitlezen van testdata bestand en filteren van data
with open('Data/TestDataset.csv', 'r') as csvFile:
    csv_file = list(csv.reader(csvFile))
    available_test_symptoms = list(
        map(lambda v: v.strip().lower(), csv_file[0]))[2:-1]
    testData = csv_file[1:]

test_features = []
test_labels = []

train_features = []
train_labels = []

# opsplitsen van labels en features voor training data
for item in trainData:
    train_labels.append(item[-1])
    train_features.append(item[:-1].copy())

# opsplitsen van labels en features voor test data
for item in testData:
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())


clf = RandomForestClassifier(n_estimators=amount_trees, random_state=0)
clf.fit(train_features, train_labels)
pred = clf.predict(test_features)
print('Accuraatheid is: ' + str(metrics.accuracy_score(test_labels, pred)))

while True:
    print("\nWat is uw geslacht? (0 voor VROUW, 1 voor MAN)")
    geslacht = int(input(""))

    print("\nWat is uw leeftijd?")
    leeftijd = int(input(""))

    symptoms = None
    while symptoms is None:
        print("\nDe beschikbare symptomen zijn:")
        print(", ".join(available_training_symptoms))
        print("\nVul uw symptomen in, gescheiden door een comma:")
        symptoms = list(map(lambda v: v.strip().lower(), input("").split(",")))

        existing_symptoms = list(
            filter(lambda v: v in available_training_symptoms, symptoms))

        if len(existing_symptoms) != len(symptoms):
            print("\nU mag alleen symptomen opnoemen die bij ons geregistreerd zijn. De symptomen die u invulde maar niet bij ons geregistreerd staan zijn:")
            not_existing_symptoms = list(
                set(symptoms) - set(existing_symptoms))
            print(", ".join(not_existing_symptoms))

            symptoms = None
    symptoms_array = [geslacht, leeftijd]
    for available_symptom in available_training_symptoms:
        symptoms_array.append(1 if available_symptom in symptoms else 0)

    prediction = int(clf.predict([symptoms_array])[0])

    print("\n\n--> De applicatie geeft aan dat u waarschijnlijk de volgende ziekte heeft:")
    print(available_diseases[prediction])
    print("\nUw ziekte is bepaald. Druk op 'j' om de applicatie te herstarten.")
    again = input("")
    if again.upper() != "J":
        break

print("\nU heeft aangegeven dat u geen behoefte meer heeft om de applicatie te herstarten. Fijne dag nog!")
