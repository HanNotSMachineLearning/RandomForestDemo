# Testresultaten - ...

In dit document staan de verschillende resultaten van het testen van het prototype uitgewerkt.

Developer: Eric Jans		

Reviewer 1:		

Reviewer 2:		



## Accuraatheid

Onder het onderdeel accuraatheid zijn een aantal verschillende zaken van het prototype getest beteft de accuraatheid van de gemaakte voorspelling.

#### Dataset grootte

Het eerste onderdeel dat getest is, is de toename van de accuraatheid van het algoritme naarmate de hoeveelheid beschikbare trainingsdata groter wordt. Dit is getest door het prototype te trainen kleinere hoeveelheden data van de volledige dataset. 

De onderstaande tabel bevat de waardes van de gemiddelde accuraatheids percentage van de applicatie die zijn gevonden door de applicatie te testen met de testdataset.
In de onderstaande tabel is ervan uit gegaan dat de standaard hoeveelheid decision trees, namelijk 25, gebruikt is. 

| Percentage data          | Developer | Reviewer 1 | Reviewer 2 |
| ------------------------ | --------- | ---------- | ---------- |
| **25% van de dataset**   |  0,66666  |            |            |
| **50% van de dataset**   |  0,86667  |            |            |
| **75% van de dataset**   |  0,86667  |            |            |
| **100%  van de dataset** |  0,86667  |            |            |

#### Aantal decision trees

In dit specifieke algoritme zijn er ook meerdere decision trees die samen een antwoord geven. Het belangrijk om te kijken tot welk punt meerdere decision trees een verschil maakt in de accuraatheid van het algoritme. Dit wordt getest met de gemaakte testdataset

| Decision trees           | Developer | Reviewer 1 | Reviewer 2 |
| ------------------------ | --------- | ---------- | ---------- |
| **1 Decision tree**      |  0,53333  |            |            |
| **5 Decision trees**     |  0,83334  |            |            |
| **10 Decision trees**    |  0,90000  |            |            |
| **25 Decision trees**    |  0,86667  |            |            |
| **50 Decision trees**    |  0,93333  |            |            |

#### Aantal ingevoerde symptomen

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan. 

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.
Ook bij deze tabellen wordt uitgegaan van de standaard 25 trees.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer            |        Man            |         23         |    Benauwdheid    |         Astma          |               Ja                |
| developer            |        Vrouw          |         20         |      Keelpijn     |         Griep          |               Nee               |
| developer            |        Vrouw          |         52         | Gebrek aan eetlust|       Verkoudheid      |               Nee               |
| developer            |        Man            |         43         |     Hoofdpijn     |       Verkoudheid      |               Nee               |
| reviewer 1           |                       |                    |                   |                        |                                 |
| reviewer 1           |                       |                    |                   |                        |                                 |
| reviewer 1           |                       |                    |                   |                        |                                 |
| reviewer 1           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom  | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ------------------ | ---------------------- | ------------------------------- |
| developer             |        Vrouw          |         26         | Hoesten, Koorts    |         Griep          |              Nee                |
| developer             |         Man           |         51         | Hoofdpijn, Hoesten |     Longontsteking     |              Nee                |
| developer             |        Vrouw          |         32         | Niezen, Hoesten    |       Verkoudheid      |              Ja                 |
| developer             |         Man           |          6         |Koorts, Vermoeidheid|       Verkoudheid      |              Ja                 |
| reviewer 1            |                       |                    |                    |                        |                                 |
| reviewer 1            |                       |                    |                    |                        |                                 |
| reviewer 1            |                       |                    |                    |                        |                                 |
| reviewer 1            |                       |                    |                    |                        |                                 |
| reviewer 2            |                       |                    |                    |                        |                                 |
| reviewer 2            |                       |                    |                    |                        |                                 |
| reviewer 2            |                       |                    |                    |                        |                                 |
| reviewer 2            |                       |                    |                    |                        |                                 |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                       | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | --------------------------------------- | ---------------------- | ------------------------------- |
| developer             |         Man           |         23         |Koorts, Hoesten, Spierpijn               |        Bronchitis      |               Nee               |
| developer             |         Man           |          7         |Koorts, Hoesten, Spierpijn               |      Verkoudheid       |               Nee               |
| developer             |         Man           |         52         |Keelpijn, Spierpijn, Verstopte Neus      |          Griep         |               Ja                |
| developer             |        Vrouw          |         66         |Hoesten, Vermoeidheid, Gebrek aan eetlust|     Longontsteking     |               Ja                |
| reviewer 1            |                       |                    |                                         |                        |                                 |
| reviewer 1            |                       |                    |                                         |                        |                                 |
| reviewer 1            |                       |                    |                                         |                        |                                 |
| reviewer 1            |                       |                    |                                         |                        |                                 |
| reviewer 2            |                       |                    |                                         |                        |                                 |
| reviewer 2            |                       |                    |                                         |                        |                                 |
| reviewer 2            |                       |                    |                                         |                        |                                 |
| reviewer 2            |                       |                    |                                         |                        |                                 |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                  | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             |         Vrouw         |         23         | Koorts,Hoofdpijn,Hoesten,Keelpijn                  |Griep                   |Ja                               |
| developer             |         Vrouw         |         33         | Hoesten,Spierpijn,Koorts,Piepende ademhaling       |Bronchitis              |Ja                               |
| developer             |         Man           |         41         | Kortademig,Benauwdheid, Piepende ademhaling, Niezen|Astma                   |Ja                               |
| developer             |         Vrouw         |         16         | Hoesten,Niezen,Vermoeidheid,Hoofdpijn              |Verkoudheid             |Ja                               |
| reviewer 1            |                       |                    |                                                    |                        |                                 |
| reviewer 1            |                       |                    |                                                    |                        |                                 |
| reviewer 1            |                       |                    |                                                    |                        |                                 |
| reviewer 1            |                       |                    |                                                    |                        |                                 |
| reviewer 2            |                       |                    |                                                    |                        |                                 |
| reviewer 2            |                       |                    |                                                    |                        |                                 |
| reviewer 2            |                       |                    |                                                    |                        |                                 |
| reviewer 2            |                       |                    |                                                    |                        |                                 |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                          | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ---------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             |       Man             |         12         |Kortademig, Benauwdheid,Piepende ademhaling, Hoesten, Koorts|Astma                   |Ja                               |
| developer             |       Vrouw           |          8         |Koorts,Hoesten,Niezen,Spierpijn,Keelpijn                    |Verkoudheid             |Ja                               |
| developer             |       Vrouw           |         41         |Koorts,Hoesten,Hoofdpijn,Keelpijn,Spierpijn                 |Griep                   |Ja                               |
| developer             |       Man             |          5         |Neusvleugelen, Koorts, Kortademig,Vermoeidheid,Hoesten      |Longontsteking          |Ja                               |
| reviewer 1            |                       |                    |                                                            |                        |                                 |
| reviewer 1            |                       |                    |                                                            |                        |                                 |
| reviewer 1            |                       |                    |                                                            |                        |                                 |
| reviewer 1            |                       |                    |                                                            |                        |                                 |
| reviewer 2            |                       |                    |                                                            |                        |                                 |
| reviewer 2            |                       |                    |                                                            |                        |                                 |
| reviewer 2            |                       |                    |                                                            |                        |                                 |
| reviewer 2            |                       |                    |                                                            |                        |                                 |