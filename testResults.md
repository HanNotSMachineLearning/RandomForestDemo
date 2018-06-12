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
| developer            | Man                   | 23                 | Benauwdheid         | Astma                  | J                               |
| developer            | Vrouw                 | 20                 | Keelpijn            | Griep                  | N (verkoudheid)                 |
| developer            | Vrouw                 | 52                 | Gebrek aan eetlust  | Verkoudheid            | N (bronchitis)                  |
| developer            | Man                   | 43                 | Hoofdpijn           | Verkoudheid            | N (griep)                       |
| reviewer 1           | man                   | 85                 | koorts              | griep                  | n (bronchitis)                  |
| reviewer 1           | vrouw                 | 35                 | vermoeidheid        | verkoudheid            | j                               |
| reviewer 1           | vrouw                 | 73                 | keelpijn            | griep                  | j                               |
| reviewer 1           | vrouw                 | 90                 | hoofdpijn           | verkoudheid            | n (griep)                       |
| reviewer 2           | man                   | 9                  | verstopte neus      | verkoudheid            | j                               |
| reviewer 2           | man                   | 29                 | piepende ademhaling | astma                  | j                               |
| reviewer 2           | vrouw                 | 38                 | Pijn bij borst      | longontsteking         | j                               |
| reviewer 2           | vrouw                 | 10                 | Hoge slijmproductie | Bronchitis             | j                               |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------- | ---------------------- | ------------------------------- |
| developer             | Vrouw                 | 26                 | Hoesten, Koorts                     | Griep                  | Nee                             |
| developer             | Man                   | 51                 | Hoofdpijn, Hoesten                  | Longontsteking         | Nee                             |
| developer             | Vrouw                 | 32                 | Niezen, Hoesten                     | Verkoudheid            | Ja                              |
| developer             | Man                   | 6                  | Koorts, Vermoeidheid                | Verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 21                 | hoesten, niezen                     | verkoudheid            | j                               |
| reviewer 1            | man                   | 43                 | hoesten, hoge slijmproductie        | bronchitis             | j                               |
| reviewer 1            | vrouw                 | 62                 | keelpijn, verstopte neus            | verkoudheid            | n (griep)                       |
| reviewer 1            | man                   | 18                 | spierpijn, keelpijn                 | griep                  | j                               |
| reviewer 2            | man                   | 10                 | hoge slijmproductie, verstopte neus | bronchitis             | j                               |
| reviewer 2            | man                   | 45                 | neusvleugelen, hoofdpijn            | verkoudheid            | n (griep)                       |
| reviewer 2            | vrouw                 | 37                 | Hoofdpijn, Vermoeidheid             | griep                  | n (verkoudheid)                 |
| reviewer 2            | vrouw                 | 15                 | piepende ademhaling, kortademig     | longontsteking         | n (astma)                       |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                             | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | --------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Man                   | 23                 | Koorts, Hoesten, Spierpijn                    | Bronchitis             | Nee                             |
| developer             | Man                   | 7                  | Koorts, Hoesten, Spierpijn                    | Verkoudheid            | Nee                             |
| developer             | Man                   | 52                 | Keelpijn, Spierpijn, Verstopte Neus           | Griep                  | Ja                              |
| developer             | Vrouw                 | 66                 | Hoesten, Vermoeidheid, Gebrek aan eetlust     | Longontsteking         | Ja                              |
| reviewer 1            | vrouw                 | 33                 | hoesten, koorts, kortademig                   | longontsteking         | n (astma)                       |
| reviewer 1            | man                   | 22                 | hoesten, niezen, spierpijn                    | verkoudheid            | j                               |
| reviewer 1            | vrouw                 | 44                 | kortademig, benauwdheid, piepende ademhaling  | astma                  | j                               |
| reviewer 1            | man                   | 53                 | keelpijn, spierpijn, gebrek aan eetlust       | griep                  | j                               |
| reviewer 2            | man                   | 16                 | verstopte neus, spierpijn, keelpijn           | verkoudheid            | j                               |
| reviewer 2            | man                   | 33                 | kortademig, benauwdheid, hoesten              | astma                  | j                               |
| reviewer 2            | vrouw                 | 62                 | Keelpijn, Hoge slijmproductie, Pijn bij borst | griep                  | n (bronchitis)                  |
| reviewer 2            | vrouw                 | 13                 | hoesten, piepende ademhaling, kortademig      | bronchitis             | n (astma)                       |

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
| reviewer 2            | man                   | 14                 | Hoesten, Keelpijn, Pijn bij borst, Piepende ademhaling      | bronchitis             | n (astma)                       |
| reviewer 2            | man                   | 55                 | hoesten, niezen, spierpijn, hoofdpijn                       | verkoudheid            | j                               |
| reviewer 2            | vrouw                 | 34                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust    | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 17                 | Gebrek aan eetlust, Hoesten, Koorts, Niezen                 | griep                  | n (verkoudheid)                 |

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
| reviewer 2            | man                   | 20                 | Hoesten, Keelpijn, Hoge slijmproductie, Pijn bij borst, Kortademig   | longontsteking         | n (bronchitis)                  |
| reviewer 2            | man                   | 13                 | Neusvleugelen, Koorts, Kortademig,Vermoeidheid,Hoesten               | longontsteking         | j                               |
| reviewer 2            | vrouw                 | 12                 | Kortademig, Benauwdheid, Hoesten, Piepende ademhaling, Spierpijn     | astma                  | j                               |
| reviewer 2            | vrouw                 | 27                 | Koorts, Hoesten, Hoofdpijn, Keelpijn, Hoge slijmproductie            | griep                  | n (bronchitis)                  |



#### Aantal ingevoerde symptomen bij 50 trees

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.
Ook bij deze tabellen wordt uitgegaan van 50 trees.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ------------------- | ---------------------- | ------------------------------- |
| developer            | Man                   | 23                 | Benauwdheid         | Astma                  | Ja                              |
| developer            | Vrouw                 | 20                 | Keelpijn            | Griep                  | Ja                              |
| developer            | Vrouw                 | 52                 | Gebrek aan eetlust  | Verkoudheid            | Ja                              |
| developer            | Man                   | 43                 | Hoofdpijn           | Verkoudheid            | Nee(griep)                      |
| reviewer 1           | man                   | 85                 | koorts              | griep                  | Nee(bronchitis)                 |
| reviewer 1           | vrouw                 | 35                 | vermoeidheid        | verkoudheid            | Ja                              |
| reviewer 1           | vrouw                 | 73                 | keelpijn            | griep                  | Ja                              |
| reviewer 1           | vrouw                 | 90                 | hoofdpijn           | verkoudheid            | Nee(griep)                      |
| reviewer 2           | man                   | 9                  | verstopte neus      | verkoudheid            | Ja                              |
| reviewer 2           | man                   | 29                 | piepende ademhaling | astma                  | Ja                              |
| reviewer 2           | vrouw                 | 38                 | Pijn bij borst      | longontsteking         | Ja                              |
| reviewer 2           | vrouw                 | 10                 | Hoge slijmproductie | Bronchitis             | Ja                              |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                   | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------- | ---------------------- | ------------------------------- |
| developer             | Vrouw                 | 26                 | Hoesten, Koorts                     | Griep                  | Nee(bronchitis)                 |
| developer             | Man                   | 51                 | Hoofdpijn, Hoesten                  | Longontsteking         | Nee(griep)                      |
| developer             | Vrouw                 | 32                 | Niezen, Hoesten                     | Verkoudheid            | Ja                              |
| developer             | Man                   | 6                  | Koorts, Vermoeidheid                | Verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 21                 | hoesten, niezen                     | verkoudheid            | Ja                              |
| reviewer 1            | man                   | 43                 | hoesten, hoge slijmproductie        | bronchitis             | Ja                              |
| reviewer 1            | vrouw                 | 62                 | keelpijn, verstopte neus            | verkoudheid            | Nee(griep)                      |
| reviewer 1            | man                   | 18                 | spierpijn, keelpijn                 | griep                  | Ja                              |
| reviewer 2            | man                   | 10                 | hoge slijmproductie, verstopte neus | bronchitis             | Ja                              |
| reviewer 2            | man                   | 45                 | neusvleugelen, hoofdpijn            | verkoudheid            | Nee(griep)                      |
| reviewer 2            | vrouw                 | 37                 | Hoofdpijn, Vermoeidheid             | griep                  | Nee(verkoudheid)                |
| reviewer 2            | vrouw                 | 15                 | piepende ademhaling, kortademig     | longontsteking         | Nee(astma)                      |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                             | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | --------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Man                   | 23                 | Koorts, Hoesten, Spierpijn                    | Bronchitis             | Nee(griep)                      |
| developer             | Man                   | 7                  | Koorts, Hoesten, Spierpijn                    | Verkoudheid            | Nee(bronchitis)                 |
| developer             | Man                   | 52                 | Keelpijn, Spierpijn, Verstopte Neus           | Griep                  | Ja                              |
| developer             | Vrouw                 | 66                 | Hoesten, Vermoeidheid, Gebrek aan eetlust     | Longontsteking         | Ja                              |
| reviewer 1            | vrouw                 | 33                 | hoesten, koorts, kortademig                   | longontsteking         | Nee(astma)                      |
| reviewer 1            | man                   | 22                 | hoesten, niezen, spierpijn                    | verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 44                 | kortademig, benauwdheid, piepende ademhaling  | astma                  | Ja                              |
| reviewer 1            | man                   | 53                 | keelpijn, spierpijn, gebrek aan eetlust       | griep                  | Ja                              |
| reviewer 2            | man                   | 16                 | verstopte neus, spierpijn, keelpijn           | verkoudheid            | Ja                              |
| reviewer 2            | man                   | 33                 | kortademig, benauwdheid, hoesten              | astma                  | Ja                              |
| reviewer 2            | vrouw                 | 62                 | Keelpijn, Hoge slijmproductie, Pijn bij borst | griep                  | Nee(longontsteking)             |
| reviewer 2            | vrouw                 | 13                 | hoesten, piepende ademhaling, kortademig      | bronchitis             | Nee(astma)                      |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                           | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Vrouw                 | 23                 | Koorts,Hoofdpijn,Hoesten,Keelpijn                           | Griep                  | Ja                              |
| developer             | Vrouw                 | 33                 | Hoesten,Spierpijn,Koorts,Piepende ademhaling                | Bronchitis             | Ja                              |
| developer             | Man                   | 41                 | Kortademig,Benauwdheid, Piepende ademhaling, Niezen         | Astma                  | Ja                              |
| developer             | Vrouw                 | 16                 | Hoesten,Niezen,Vermoeidheid,Hoofdpijn                       | Verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 53                 | neusvleugelen, kortademig, hoofdpijn, vermoeidheid          | longontsteking         | Ja                              |
| reviewer 1            | man                   | 43                 | hoesten, benauwdheid, kortademig, piepende ademhaling       | astma                  | Ja                              |
| reviewer 1            | vrouw                 | 56                 | spierpijn, keelpijn, hoesten, hoofdpijn                     | griep                  | Ja                              |
| reviewer 1            | man                   | 33                 | pijn bij borst, hoofdpijn, vermoeidheid, gebrek aan eetlust | longontsteking         | Ja                              |
| reviewer 2            | man                   | 14                 | Hoesten, Keelpijn, Pijn bij borst, Piepende ademhaling      | bronchitis             | Nee(astma)                      |
| reviewer 2            | man                   | 55                 | hoesten, niezen, spierpijn, hoofdpijn                       | verkoudheid            | Ja                              |
| reviewer 2            | vrouw                 | 34                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust    | longontsteking         | Ja                              |
| reviewer 2            | vrouw                 | 17                 | Gebrek aan eetlust, Hoesten, Koorts, Niezen                 | griep                  | Nee(verkoudheid)                |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                    | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | Man                   | 12                 | Kortademig, Benauwdheid,Piepende ademhaling, Hoesten, Koorts         | Astma                  | Ja                              |
| developer             | Vrouw                 | 8                  | Koorts,Hoesten,Niezen,Spierpijn,Keelpijn                             | Verkoudheid            | Ja                              |
| developer             | Vrouw                 | 41                 | Koorts,Hoesten,Hoofdpijn,Keelpijn,Spierpijn                          | Griep                  | Ja                              |
| developer             | Man                   | 5                  | Neusvleugelen, Koorts, Kortademig,Vermoeidheid,Hoesten               | Longontsteking         | Ja                              |
| reviewer 1            | man                   | 44                 | koorts, kortademig, vermoeidheid, hoesten, neusvleugelen             | longontsteking         | Ja                              |
| reviewer 1            | man                   | 63                 | keelpijn, hoofdpijn, spierpijn, niezen, hoesten                      | verkoudheid            | Ja                              |
| reviewer 1            | vrouw                 | 66                 | gebrek aan eetlust, vermoeidheid, pijn bij borst, koorts, hoesten    | longontsteking         | Ja                              |
| reviewer 1            | man                   | 23                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis             | Ja                              |
| reviewer 2            | man                   | 20                 | Hoesten, Keelpijn, Hoge slijmproductie, Pijn bij borst, Kortademig   | longontsteking         | Ja                              |
| reviewer 2            | man                   | 13                 | Neusvleugelen, Koorts, Kortademig,Vermoeidheid,Hoesten               | longontsteking         | Ja                              |
| reviewer 2            | vrouw                 | 12                 | Kortademig, Benauwdheid, Hoesten, Piepende ademhaling, Spierpijn     | astma                  | Ja                              |
| reviewer 2            | vrouw                 | 27                 | Koorts, Hoesten, Hoofdpijn, Keelpijn, Hoge slijmproductie            | griep                  | Ja                              |
