# Documentatie Random/Decision forest algoritme prototype

Dit prototype is onderdeel van een reeks van prototypes die gebouwd zijn ter ondersteuning van deelvraag 8: 'Welke algoritmes van machine learning sluiten het beste aan op deze casus? ' van het onderzoek 'Machine learning voor de huisarts'. Door middel van deze prototypes wordt getest welk machine learning algoritme het meest geschikt is om te gebruiken binnen de casus van het onderzoek. Alle prototypes worden geschreven in Python en maken gebruik van het sklearn machine learning framework.



## Algoritme

Random/Decision forest is een enhanced decision tree algoritme, dit wil zeggen dat het een verbetering op de decision tree is.
De verbetering in dit algoritme is te vinden in de hoeveelheid decision trees. In dit algoritme kan er aangegeven worden hoeveel decision trees een voorspelling moeten gaan doen. Vervolgens wordt door een stem principe het uiteindelijke antwoord gekozen. Dus als twee trees A zeggen, vier zeggen B en 12 zeggen C, wil zeggen dat het algehele antwoord C wordt.



## Trainingsdata

Om het machine learning algoritme te trainen wordt er gebruik gemaakt van een dataset bestaande uit ziektes en hun bijbehorende symptomen. De dataset is terug te vinden in de folder `Data`  binnen de projectfolder van het prototype.



## Afhankelijkheden

Zoals eerder genoemd is het prototype geschreven in python, om precies te zijn versie 3.6. Daarnaast wordt PIP versie 10.0 gebruikt voor het installeren en beheren van de verschillende externe packages die gebruikt worden in het prototype. Het is dus van belang dat de volgende zaken aanwezig zijn op machine waarop het prototype gedraaid wordt.

- Python versie 3.6   	            (https://www.python.org/downloads/release/python-365/)
- Pip versie 10.0                   (https://pip.pypa.io/en/stable/installing/)

```
!-- LETOP --!
Het is van belang dat python wordt toegevoegd aan je Windows Path variable.
Hiervoor is een optie te vinden in de installatiewizzard van Python.
```

## Installatie

Om het prototype te draaien dienen er een aantal externe packages geïnstalleerd te worden.
Al deze packages zijn te installeren door het commando `pip install -r requirements.txt --user` uit te voeren in een Terminal venster in de projectfolder van het prototype. Dit commando zorgt ervoor dat alle benodigde packages in een keer gedownload worden.

- scikit-learn versie 0.19.1        (http://scikit-learn.org)
- Numpy versie 1.14.3               (http://www.numpy.org/)

## Opstarten

Het prototype kan gestart worden door het commando `python prototype.py` uit te voeren in een Terminal verster in de projectfolder van het prototype.

## Code

```python
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
```

&copy;2018 - NotS project machine learning 2018
