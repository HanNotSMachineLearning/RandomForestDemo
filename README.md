# Documentatie Random/Decision forest algoritme prototype

Dit prototype is onderdeel van een reeks van prototypes die gebouwd zijn ter ondersteuning van deelvraag 8: 'Welke algoritmes van machine learning sluiten het beste aan op deze casus? ' van het onderzoek 'Machine learning voor de huisarts'. Door middel van deze prototypes wordt getest welk machine learning algoritme het meest geschikt is om te gebruiken binnen de casus van het onderzoek. Alle prototypes worden geschreven in Python en maken gebruik van het TensorFlow machine learning framework.



## Algoritme

Random/Decision forest is een enhanced decision tree algoritme, dit wil zeggen dat het een verbetering op de decision tree is.
De verbetering in dit algoritme is te vinden in de hoeveelheid decision trees. In dit algoritme kan er aangegeven worden hoeveel decision trees een voorspelling moeten gaan doen. Vervolgens wordt door een stem principe het uiteindelijke antwoord gekozen. Dus als twee trees A zeggen, vier zeggen B en 12 zeggen C, wil zeggen dat het algehele antwoord C wordt.



## Trainingsdata

Om het machine learning algoritme te trainen wordt er gebruik gemaakt van een dataset bestaande uit ziektes en hun bijbehorende symptomen. De dataset is terug te vinden in de folder `Data`  binnen de projectfolder van het prototype.



## Afhankelijkheden

Zoals eerder genoemd is het prototype geschreven in python, om precies te zijn versie 3.6. Daarnaast wordt PIP versie 10.0 gebruikt voor het installeren en beheren van de verschillende externe packages die gebruikt worden in het prototype. Het is dus van belang dat de volgende zaken aanwezig zijn op machine waarop het prototype gedraaid wordt.

- Python versie 3.6   	            (https://www.python.org/downloads/release/python-365/)
- Pip versie 10.0                   (https://pip.pypa.io/en/stable/installing/)
- scikit-learn versie 0.19.1        (http://scikit-learn.org)
- Numpy versie 1.14.3               (http://www.numpy.org/)

```
!-- LETOP --!
Het is van belang dat python wordt toegevoegd aan je Windows Path variable.
Hiervoor is een optie te vinden in de installatiewizzard van Python.
```

## Installatie

Om het prototype te draaien dienen er een aantal externe packages geïnstalleerd te worden.
Al deze packages zijn te installeren door het commando `pip install -r requirements.txt --user` uit te voeren in een Terminal venster in de projectfolder van het prototype. Dit commando zorgt ervoor dat alle benodigde packages in een keer gedownload worden.

## Opstarten

Het prototype kan gestart worden door het commando `python prototype.py` uit te voeren in een Terminal verster in de projectfolder van het prototype.

&copy;2018 - NotS project machine learning 2018