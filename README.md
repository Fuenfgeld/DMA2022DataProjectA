# COVDAF

## Kurzbeschreibung
Im Rahmen dieses Projekts soll die Frage beantwortet werden, ob es einen Zusammenhang zwischen der Influenzaimpfung und der Anzahl der COVID-19 Todesfälle gibt. Zusätzlich soll beantwortet werden, ob verschiedene Ethnien stärker von dem Virus betroffen sind.
Die Vorstellung dieses Projektes in Form eines Videos ist HIER!!!!!!! zu finden.

## Daten
Die Daten, die zur Beantwortung der Frage genutzt werden, stammen aus dem Sacred Heart Hospital in San DiFrangeles, Kalifornien. Daten, die genutzt werden können, um Patienten zu identifizieren, wurden anonymisiert. 
* [Dieser](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Beschreibung-der-zu-erhebenden-Forschungsdaten) Link führt zur Beschreibung der zu erhebenden Forschungsdaten. Dort sind auch Informationen über die [Quelldaten](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Quelldaten) und den [ETL Prozess](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/ETL-Prozess) zu finden.
* Ausführliche Informationen über die Daten sind im [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenmanagementplan) zu finden. 
* Informationen über die Datenqualität und -Integrität sind [hier](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenqualit%C3%A4t-und-Datenintegrit%C3%A4t) auffindbar
* Wie die Daten der Patienten geschützt werden, ist in der [Datenschutzfolgeabschätztung](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenschutzfolgeabsch%C3%A4tzung) nachzulesen.

## Grafische Darstellung des Projektes
Eine Übersicht über die gesamte Projektplanung und ihren Verlauf finden Sie im [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenmanagementplan).
![Datenflussdiagramm](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Datenflussdiagramm.png)

## Analyse
Die Analyse wurde mithilfe von Pandas in Python durchgeführt. Die Ergebnisse werden mit Seaborn geplottet. Wie die Analyse nachvollzogen werden kann, ist im Abschnitt [Systemumgebung](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Systemumgebung) zu finden.

Die Analyse kann auch anhand des Google [Colaboratories](https://colab.research.google.com/github/Fuenfgeld/DMA2022DataProjectA/blob/main/Code/Create_Data_Warehouse_and_Analyse.ipynb) persönlich nachvollzogen werden. 

## Ergebniszusammenfassung
Durch die Analyse erigbt sich, dass prozentual mehr Menschen an COVID-19 sterben, als in unserem Datensatz generell geimpft sind. In der folgenden Grafik, ist die Verteilung der gegen Influenza geimpften Patienten zu den nicht gegen Influenza Patienten im Datensatz sichtbar
![Kuchendiagramm alle Patienten, 99% geimpfte, 1% ungeimpfte (Bezogen auf die Influenza Impfung)](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/ungeimpft_geimpft_alle.png)

In der zweiten Grafik wird deutlich, dass 19% der an Corona gestorbenen Patienten nicht gegen Influenza geimpft wurden.
![Kuchendiagramm gestorbene Patienten, 81% geimpfte, 19% ungeimpfte (Bezogen auf die Influenza Impfung)](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/ungeimpft_geimpft_gestorben.png)

Aufgrund mangelnder Daten können wir jedoch nicht bestätigen, dass ein Zusammenhang herrscht. Beispielweise könnnten auch Menschen, die sich nicht gegen Influenza impfen lassen auch eher nicht gegen COVID-19 impfen lassen. 

Betrachtet man die verschiedenen Ethnien, so lässt sich feststellen, dass die Bevölkerungsgruppe "Black, nonhispanic" prozentual gesehen stärker betroffen war als andere Gruppen. Die folgenden beiden Grafiken stellen einmal in der erstne Grafik die Verteilung der Ethnien bei allen Patienten und in der zweiten Grafik die Verteilung der Ethnien bei den gestorbenen Patienten dar. 

![Balkendiagramm Ethnien aller Patienten](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/verteilung_ethnien_alle.png)

 
![Balkendiagramm Ethnien aller Patienten](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/verteilung_ethnien_gestorben.png)

Besonders auffällig ist, dass die Bevölkerungsgruppe ("asian, nonhispanic") im Balkendiagramm der Verteilung der Ethnien unter den gestorbenen nicht vertreten ist.


Disclaimer: In dem Projekt wurden synthetische Daten verwendet. Keine echten Patienten Data (siehe https://github.com/synthetichealth/synthea)

