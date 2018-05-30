# Testresultaten - ...

In dit document staan de verschillende resultaten van het testen van het prototype uitgewerkt.

Developer: Eric Jans

Reviewer 1: Robin Bozan

Reviewer 2: Rahmat Syamsuddin

## Accuraatheid

Onder het onderdeel accuraatheid zijn een aantal verschillende zaken van het prototype getest beteft de accuraatheid van de gemaakte voorspelling.

#### Dataset grootte

Het eerste onderdeel dat getest is, is de toename van de accuraatheid van het algoritme naarmate de hoeveelheid beschikbare trainingsdata groter wordt. Dit is getest door het prototype te trainen kleinere hoeveelheden data van de volledige dataset.

De onderstaande tabel bevat de waardes van de gemiddelde accuraatheids percentage van de applicatie die zijn gevonden door de applicatie te testen met de testdataset.
In de onderstaande tabel is ervan uit gegaan dat de standaard hoeveelheid decision trees, namelijk 25, gebruikt is.

| Percentage data         | Developer | Reviewer 1 | Reviewer 2 |
| ----------------------- | --------- | ---------- | ---------- |
| **25% van de dataset**  | 0,66666   | 66,67 %    | 66,67%     |
| **50% van de dataset**  | 0,86667   | 86,67 %    | 86,67%     |
| **75% van de dataset**  | 0,86667   | 86,67 %    | 86,67%     |
| **100% van de dataset** | 0,86667   | 86,67 %    | 86,67%     |

#### Aantal decision trees

In dit specifieke algoritme zijn er ook meerdere decision trees die samen een antwoord geven. Het belangrijk om te kijken tot welk punt meerdere decision trees een verschil maakt in de accuraatheid van het algoritme. Dit wordt getest met de gemaakte testdataset

| Decision trees        | Developer | Reviewer 1 | Reviewer 2 |
| --------------------- | --------- | ---------- | ---------- |
| **1 Decision tree**   | 0,53333   | 43,33 %    | 53,33%     |
| **5 Decision trees**  | 0,83334   | 83,33 %    | 83,33%     |
| **10 Decision trees** | 0,90000   | 90 %       | 90,00%     |
| **25 Decision trees** | 0,86667   | 86,67 %    | 86,67%     |
| **50 Decision trees** | 0,93333   | 93,33 %    | 93,33%     |

#### Aantal ingevoerde symptomen

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.
Ook bij deze tabellen wordt uitgegaan van de standaard 25 trees.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom  | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ------------------ | ---------------------- | ------------------------------- |
| developer            | Man                   | 23                 | Benauwdheid        | Astma                  | Ja                              |
| developer            | Vrouw                 | 20                 | Keelpijn           | Griep                  | Nee                             |
| developer            | Vrouw                 | 52                 | Gebrek aan eetlust | Verkoudheid            | Nee                             |
| developer            | Man                   | 43                 | Hoofdpijn          | Verkoudheid            | Nee                             |
| reviewer 1           | man                   | 85                 | koorts             | griep                  | n (bronchitis)                  |
| reviewer 1           | vrouw                 | 35                 | vermoeidheid       | verkoudheid            | j                               |
| reviewer 1           | vrouw                 | 73                 | keelpijn           | griep                  | j                               |
| reviewer 1           | vrouw                 | 90                 | hoofdpijn          | verkoudheid            | n (griep)                       |
| reviewer 2           |                       |                    |                    |                        |                                 |
| reviewer 2           |                       |                    |                    |                        |                                 |
| reviewer 2           |                       |                    |                    |                        |                                 |
| reviewer 2           |                       |                    |                    |                        |                                 |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom            | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ---------------------------- | ---------------------- | ------------------------------- |
| developer             | Vrouw                 | 26                 | Hoesten, Koorts              | Griep                  | Nee                             |
| developer             | Man                   | 51                 | Hoofdpijn, Hoesten           | Longontsteking         | Nee                             |
| developer             | Vrouw                 | 32                 | Niezen, Hoesten              | Verkoudheid            | Ja                              |
| developer             | Man                   | 6                  | Koorts, Vermoeidheid         | Verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 21                 | hoesten, niezen              | verkoudheid            | j                               |
| reviewer 1            | man                   | 43                 | hoesten, hoge slijmproductie | bronchitis             | j                               |
| reviewer 1            | vrouw                 | 62                 | keelpijn, verstopte neus     | verkoudheid            | n (griep)                       |
| reviewer 1            | man                   | 18                 | spierpijn, keelpijn          | griep                  | j                               |
| reviewer 2            |                       |                    |                              |                        |                                 |
| reviewer 2            |                       |                    |                              |                        |                                 |
| reviewer 2            |                       |                    |                              |                        |                                 |
| reviewer 2            |                       |                    |                              |                        |                                 |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                            | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Man                   | 23                 | Koorts, Hoesten, Spierpijn                   | Bronchitis             | Nee                             |
| developer             | Man                   | 7                  | Koorts, Hoesten, Spierpijn                   | Verkoudheid            | Nee                             |
| developer             | Man                   | 52                 | Keelpijn, Spierpijn, Verstopte Neus          | Griep                  | Ja                              |
| developer             | Vrouw                 | 66                 | Hoesten, Vermoeidheid, Gebrek aan eetlust    | Longontsteking         | Ja                              |
| reviewer 1            | vrouw                 | 33                 | hoesten, koorts, kortademig                  | longontsteking         | n (astma)                       |
| reviewer 1            | man                   | 22                 | hoesten, niezen, spierpijn                   | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 44                 | kortademig, benauwdheid, piepende ademhaling | astma                  | j                               |
| reviewer 1            | man                   | 53                 | keelpijn, spierpijn, gebrek aan eetlust      | griep                  | j                               |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                           | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Vrouw                 | 23                 | Koorts,Hoofdpijn,Hoesten,Keelpijn                           | Griep                  | Ja                              |
| developer             | Vrouw                 | 33                 | Hoesten,Spierpijn,Koorts,Piepende ademhaling                | Bronchitis             | Ja                              |
| developer             | Man                   | 41                 | Kortademig,Benauwdheid, Piepende ademhaling, Niezen         | Astma                  | Ja                              |
| developer             | Vrouw                 | 16                 | Hoesten,Niezen,Vermoeidheid,Hoofdpijn                       | Verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 53                 | neusvleugelen, kortademig, hoofdpijn, vermoeidheid          | longontsteking         | j                               |
| reviewer 1            | man                   | 43                 | hoesten, benauwdheid, kortademig, piepende ademhaling       | astma                  | j                               |
| reviewer 1            | vrouw                 | 56                 | spierpijn, keelpijn, hoesten, hoofdpijn                     | griep                  | j                               |
| reviewer 1            | man                   | 33                 | pijn bij borst, hoofdpijn, vermoeidheid, gebrek aan eetlust | longontsteking         | j                               |
| reviewer 2            |                       |                    |                                                             |                        |                                 |
| reviewer 2            |                       |                    |                                                             |                        |                                 |
| reviewer 2            |                       |                    |                                                             |                        |                                 |
| reviewer 2            |                       |                    |                                                             |                        |                                 |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                    | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Man                   | 12                 | Kortademig, Benauwdheid,Piepende ademhaling, Hoesten, Koorts         | Astma                  | Ja                              |
| developer             | Vrouw                 | 8                  | Koorts,Hoesten,Niezen,Spierpijn,Keelpijn                             | Verkoudheid            | Ja                              |
| developer             | Vrouw                 | 41                 | Koorts,Hoesten,Hoofdpijn,Keelpijn,Spierpijn                          | Griep                  | Ja                              |
| developer             | Man                   | 5                  | Neusvleugelen, Koorts, Kortademig,Vermoeidheid,Hoesten               | Longontsteking         | Ja                              |
| reviewer 1            | man                   | 44                 | koorts, kortademig, vermoeidheid, hoesten, neusvleugelen             | longontsteking         | j                               |
| reviewer 1            | man                   | 63                 | keelpijn, hoofdpijn, spierpijn, niezen, hoesten                      | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 66                 | gebrek aan eetlust, vermoeidheid, pijn bij borst, koorts, hoesten    | longontsteking         | j                               |
| reviewer 1            | man                   | 23                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis             | j                               |
| reviewer 2            |                       |                    |                                                                      |                        |                                 |
| reviewer 2            |                       |                    |                                                                      |                        |                                 |
| reviewer 2            |                       |                    |                                                                      |                        |                                 |
| reviewer 2            |                       |                    |                                                                      |                        |                                 |
