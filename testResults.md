# Testresultaten - Random/Decision forest algoritme prototype

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
| **25% van de dataset**  | 66,67%    | 66,67 %    | 66,67%     |
| **50% van de dataset**  | 86,67%    | 86,67 %    | 86,67%     |
| **75% van de dataset**  | 86,67%    | 86,67 %    | 86,67%     |
| **100% van de dataset** | 86,67%    | 86,67 %    | 86,67%     |

#### Aantal decision trees

In dit specifieke algoritme zijn er ook meerdere decision trees die samen een antwoord geven. Het belangrijk om te kijken tot welk punt meerdere decision trees een verschil maakt in de accuraatheid van het algoritme. Dit wordt getest met de gemaakte testdataset

| Decision trees        | Developer | Reviewer 1 | Reviewer 2 |
| --------------------- | --------- | ---------- | ---------- |
| **1 Decision tree**   | 53,33%    | 43,33 %    | 53,33%     |
| **5 Decision trees**  | 83,33%    | 83,33 %    | 83,33%     |
| **10 Decision trees** | 90,00%    | 90,00 %    | 90,00%     |
| **25 Decision trees** | 86,67%    | 86,67 %    | 86,67%     |
| **50 Decision trees** | 93,33%    | 93,33 %    | 93,33%     |

#### Aantal ingevoerde symptomen bij 25 trees

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.
Ook bij deze tabellen wordt uitgegaan van de standaard 25 trees.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ------------------- | ---------------------- | ------------------------------- |
| developer            | man                   | 23                 | benauwdheid         | astma                  | J                               |
| developer            | vrouw                 | 20                 | keelpijn            | griep                  | n (verkoudheid)                 |
| developer            | vrouw                 | 52                 | gebrek aan eetlust  | verkoudheid            | n (bronchitis)                  |
| developer            | man                   | 43                 | hoofdpijn           | verkoudheid            | n (griep)                       |
| reviewer 1           | man                   | 85                 | koorts              | griep                  | n (bronchitis)                  |
| reviewer 1           | vrouw                 | 35                 | vermoeidheid        | verkoudheid            | j                               |
| reviewer 1           | vrouw                 | 73                 | keelpijn            | griep                  | j                               |
| reviewer 1           | vrouw                 | 90                 | hoofdpijn           | verkoudheid            | n (griep)                       |
| reviewer 2           | man                   | 9                  | verstopte neus      | verkoudheid            | j                               |
| reviewer 2           | man                   | 29                 | piepende ademhaling | astma                  | j                               |
| reviewer 2           | vrouw                 | 38                 | pijn bij borst      | longontsteking         | j                               |
| reviewer 2           | vrouw                 | 10                 | hoge slijmproductie | bronchitis             | j                               |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 26                 | hoesten, koorts                     | griep                  | n                               |
| developer             | man                   | 51                 | hoofdpijn, hoesten                  | longontsteking         | n                               |
| developer             | vrouw                 | 32                 | niezen, hoesten                     | verkoudheid            | j                               |
| developer             | man                   | 6                  | koorts, vermoeidheid                | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 21                 | hoesten, niezen                     | verkoudheid            | j                               |
| reviewer 1            | man                   | 43                 | hoesten, hoge slijmproductie        | bronchitis             | j                               |
| reviewer 1            | vrouw                 | 62                 | keelpijn, verstopte neus            | verkoudheid            | n (griep)                       |
| reviewer 1            | man                   | 18                 | spierpijn, keelpijn                 | griep                  | j                               |
| reviewer 2            | man                   | 10                 | hoge slijmproductie, verstopte neus | bronchitis             | j                               |
| reviewer 2            | man                   | 45                 | neusvleugelen, hoofdpijn            | verkoudheid            | n (griep)                       |
| reviewer 2            | vrouw                 | 37                 | hoofdpijn, vermoeidheid             | griep                  | n (verkoudheid)                 |
| reviewer 2            | vrouw                 | 15                 | piepende ademhaling, kortademig     | longontsteking         | n (astma)                       |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                             | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | --------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 23                 | koorts, hoesten, spierpijn                    | bronchitis             | n                               |
| developer             | man                   | 7                  | koorts, hoesten, spierpijn                    | verkoudheid            | n                               |
| developer             | man                   | 52                 | keelpijn, spierpijn, verstopte neus           | griep                  | j                               |
| developer             | vrouw                 | 66                 | hoesten, vermoeidheid, gebrek aan eetlust     | longontsteking         | j                               |
| reviewer 1            | vrouw                 | 33                 | hoesten, koorts, kortademig                   | longontsteking         | n (astma)                       |
| reviewer 1            | man                   | 22                 | hoesten, niezen, spierpijn                    | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 44                 | kortademig, benauwdheid, piepende ademhaling  | astma                  | j                               |
| reviewer 1            | man                   | 53                 | keelpijn, spierpijn, gebrek aan eetlust       | griep                  | j                               |
| reviewer 2            | man                   | 16                 | verstopte neus, spierpijn, keelpijn           | verkoudheid            | j                               |
| reviewer 2            | man                   | 33                 | kortademig, benauwdheid, hoesten              | astma                  | j                               |
| reviewer 2            | vrouw                 | 62                 | keelpijn, hoge slijmproductie, pijn bij borst | griep                  | n (bronchitis)                  |
| reviewer 2            | vrouw                 | 13                 | hoesten, piepende ademhaling, kortademig      | bronchitis             | n (astma)                       |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                           | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 23                 | koorts, hoofdpijn,hoesten,keelpijn                          | griep                  | j                               |
| developer             | vrouw                 | 33                 | hoesten, spierpijn,koorts, piepende ademhaling              | bronchitis             | j                               |
| developer             | man                   | 41                 | kortademig, benauwdheid, piepende ademhaling, niezen        | astma                  | j                               |
| developer             | vrouw                 | 16                 | hoesten,niezen,vermoeidheid,hoofdpijn                       | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 53                 | neusvleugelen, kortademig, hoofdpijn, vermoeidheid          | longontsteking         | j                               |
| reviewer 1            | man                   | 43                 | hoesten, benauwdheid, kortademig, piepende ademhaling       | astma                  | j                               |
| reviewer 1            | vrouw                 | 56                 | spierpijn, keelpijn, hoesten, hoofdpijn                     | griep                  | j                               |
| reviewer 1            | man                   | 33                 | pijn bij borst, hoofdpijn, vermoeidheid, gebrek aan eetlust | longontsteking         | j                               |
| reviewer 2            | man                   | 14                 | hoesten, keelpijn, pijn bij borst, piepende ademhaling      | bronchitis             | n (astma)                       |
| reviewer 2            | man                   | 55                 | hoesten, niezen, spierpijn, hoofdpijn                       | verkoudheid            | j                               |
| reviewer 2            | vrouw                 | 34                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust    | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 17                 | gebrek aan eetlust, hoesten, koorts, niezen                 | griep                  | n (verkoudheid)                 |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                    | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 12                 | kortademig, benauwdheid, piepende ademhaling, hoesten, koorts        | astma                  | j                               |
| developer             | vrouw                 | 8                  | koorts, hoesten, niezen, spierpijn, keelpijn                         | verkoudheid            | j                               |
| developer             | vrouw                 | 41                 | koorts, hoesten, hoofdpijn, keelpijn, spierpijn                      | griep                  | j                               |
| developer             | man                   | 5                  | neusvleugelen, koorts, kortademig, vermoeidheid, hoesten             | longontsteking         | j                               |
| reviewer 1            | man                   | 44                 | koorts, kortademig, vermoeidheid, hoesten, neusvleugelen             | longontsteking         | j                               |
| reviewer 1            | man                   | 63                 | keelpijn, hoofdpijn, spierpijn, niezen, hoesten                      | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 66                 | gebrek aan eetlust, vermoeidheid, pijn bij borst, koorts, hoesten    | longontsteking         | j                               |
| reviewer 1            | man                   | 23                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis             | j                               |
| reviewer 2            | man                   | 20                 | hoesten, keelpijn, hoge slijmproductie, pijn bij borst, kortademig   | longontsteking         | n (bronchitis)                  |
| reviewer 2            | man                   | 13                 | neusvleugelen, koorts, kortademig, vermoeidheid,hoesten              | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 12                 | kortademig, benauwdheid, hoesten, piepende ademhaling, spierpijn     | astma                  | j                               |
| reviewer 2            | vrouw                 | 27                 | koorts, hoesten, hoofdpijn, keelpijn, hoge slijmproductie            | griep                  | n (bronchitis)                  |



#### Aantal ingevoerde symptomen bij 50 trees

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.
Ook bij deze tabellen wordt uitgegaan van 50 trees.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ------------------- | ---------------------- | ------------------------------- |
| developer            | man                   | 23                 | benauwdheid         | astma                  | j                               |
| developer            | vrouw                 | 20                 | keelpijn            | griep                  | j                               |
| developer            | vrouw                 | 52                 | gebrek aan eetlust  | verkoudheid            | j                               |
| developer            | man                   | 43                 | hoofdpijn           | verkoudheid            | n (griep)                      |
| reviewer 1           | man                   | 85                 | koorts              | griep                  | n (bronchitis)                 |
| reviewer 1           | vrouw                 | 35                 | vermoeidheid        | verkoudheid            | j                               |
| reviewer 1           | vrouw                 | 73                 | keelpijn            | griep                  | j                               |
| reviewer 1           | vrouw                 | 90                 | hoofdpijn           | verkoudheid            | n (griep)                      |
| reviewer 2           | man                   | 9                  | verstopte neus      | verkoudheid            | j                               |
| reviewer 2           | man                   | 29                 | piepende ademhaling | astma                  | j                               |
| reviewer 2           | vrouw                 | 38                 | pijn bij borst      | longontsteking         | j                               |
| reviewer 2           | vrouw                 | 10                 | hoge slijmproductie | bronchitis             | j                               |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 26                 | hoesten, koorts                     | griep                  | n (bronchitis)                 |
| developer             | man                   | 51                 | hoofdpijn, hoesten                  | longontsteking         | n (griep)                      |
| developer             | vrouw                 | 32                 | niezen, hoesten                     | verkoudheid            | j                               |
| developer             | man                   | 6                  | koorts, vermoeidheid                | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 21                 | hoesten, niezen                     | verkoudheid            | j                               |
| reviewer 1            | man                   | 43                 | hoesten, hoge slijmproductie        | bronchitis             | j                               |
| reviewer 1            | vrouw                 | 62                 | keelpijn, verstopte neus            | verkoudheid            | n (griep)                      |
| reviewer 1            | man                   | 18                 | spierpijn, keelpijn                 | griep                  | j                               |
| reviewer 2            | man                   | 10                 | hoge slijmproductie, verstopte neus | bronchitis             | j                               |
| reviewer 2            | man                   | 45                 | neusvleugelen, hoofdpijn            | verkoudheid            | n (griep)                      |
| reviewer 2            | vrouw                 | 37                 | hoofdpijn, vermoeidheid             | griep                  | n (verkoudheid)                |
| reviewer 2            | vrouw                 | 15                 | piepende ademhaling, kortademig     | longontsteking         | n (astma)                      |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                             | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | --------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 23                 | koorts, hoesten, spierpijn                    | bronchitis             | n (griep)                      |
| developer             | man                   | 7                  | koorts, hoesten, spierpijn                    | verkoudheid            | n (bronchitis)                 |
| developer             | man                   | 52                 | keelpijn, spierpijn, verstopte neus           | griep                  | j                               |
| developer             | vrouw                 | 66                 | hoesten, vermoeidheid, gebrek aan eetlust     | longontsteking         | j                               |
| reviewer 1            | vrouw                 | 33                 | hoesten, koorts, kortademig                   | longontsteking         | n (astma)                      |
| reviewer 1            | man                   | 22                 | hoesten, niezen, spierpijn                    | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 44                 | kortademig, benauwdheid, piepende ademhaling  | astma                  | j                               |
| reviewer 1            | man                   | 53                 | keelpijn, spierpijn, gebrek aan eetlust       | griep                  | j                               |
| reviewer 2            | man                   | 16                 | verstopte neus, spierpijn, keelpijn           | verkoudheid            | j                               |
| reviewer 2            | man                   | 33                 | kortademig, benauwdheid, hoesten              | astma                  | j                               |
| reviewer 2            | vrouw                 | 62                 | keelpijn, hoge slijmproductie, pijn bij borst | griep                  | n (longontsteking)             |
| reviewer 2            | vrouw                 | 13                 | hoesten, piepende ademhaling, kortademig      | bronchitis             | n (astma)                      |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                           | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 23                 | koorts, hoofdpijn, hoesten, keelpijn                        | griep                  | j                               |
| developer             | vrouw                 | 33                 | hoesten, spierpijn, koorts, piepende ademhaling             | bronchitis             | j                               |
| developer             | man                   | 41                 | kortademig, benauwdheid, piepende ademhaling, niezen        | astma                  | j                               |
| developer             | vrouw                 | 16                 | hoesten, niezen, vermoeidheid, hoofdpijn                    | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 53                 | neusvleugelen, kortademig, hoofdpijn, vermoeidheid          | longontsteking         | j                               |
| reviewer 1            | man                   | 43                 | hoesten, benauwdheid, kortademig, piepende ademhaling       | astma                  | j                               |
| reviewer 1            | vrouw                 | 56                 | spierpijn, keelpijn, hoesten, hoofdpijn                     | griep                  | j                               |
| reviewer 1            | man                   | 33                 | pijn bij borst, hoofdpijn, vermoeidheid, gebrek aan eetlust | longontsteking         | j                               |
| reviewer 2            | man                   | 14                 | hoesten, keelpijn, pijn bij borst, piepende ademhaling      | bronchitis             | n (astma)                      |
| reviewer 2            | man                   | 55                 | hoesten, niezen, spierpijn, hoofdpijn                       | verkoudheid            | j                               |
| reviewer 2            | vrouw                 | 34                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust    | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 17                 | gebrek aan eetlust, hoesten, koorts, niezen                 | griep                  | n (verkoudheid)                |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                    | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 12                 | kortademig, benauwdheid, piepende ademhaling, hoesten, koorts        | astma                  | j                               |
| developer             | vrouw                 | 8                  | koorts, hoesten, niezen, spierpijn, keelpijn                         | verkoudheid            | j                               |
| developer             | vrouw                 | 41                 | koorts, hoesten, hoofdpijn, keelpijn, spierpijn                      | griep                  | j                               |
| developer             | man                   | 5                  | neusvleugelen, koorts, kortademig, vermoeidheid, hoesten             | longontsteking         | j                               |
| reviewer 1            | man                   | 44                 | koorts, kortademig, vermoeidheid, hoesten, neusvleugelen             | longontsteking         | j                               |
| reviewer 1            | man                   | 63                 | keelpijn, hoofdpijn, spierpijn, niezen, hoesten                      | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 66                 | gebrek aan eetlust, vermoeidheid, pijn bij borst, koorts, hoesten    | longontsteking         | j                               |
| reviewer 1            | man                   | 23                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis             | j                               |
| reviewer 2            | man                   | 20                 | hoesten, keelpijn, hoge slijmproductie, pijn bij borst, kortademig   | longontsteking         | j                               |
| reviewer 2            | man                   | 13                 | neusvleugelen, koorts, kortademig, vermoeidheid, hoesten             | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 12                 | kortademig, benauwdheid, hoesten, piepende ademhaling, spierpijn     | astma                  | j                               |
| reviewer 2            | vrouw                 | 27                 | koorts, hoesten, hoofdpijn, keelpijn, hoge slijmproductie            | griep                  | j                               |
