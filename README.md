# COVDAF

## Kurzbeschreibung
Im Rahmen dieses Projekts soll die Frage beantwortet werden, ob es einen Zusammenhang zwischen der Influenzaimpfung und der Anzahl der COVID-19 Todesfälle gibt. Zusätzlich soll beantwortet werden, ob verschiedene Ethnien stärker von dem Virus betroffen sind.

## Daten
Die Daten, die zur Beantwortung der Frage genutzt werden, stammen aus dem Sacred Heart Hospital in San DiFrangeles, Kalifornien. Daten, die genutzt werden können, um Patienten zu identifizieren, wurden anonymisiert. 
* Ausführliche Informationen über die Daten sind im [Datenschutzmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenmanagementplan) zu finden. 
* Informationen über die Datenqualität und -Integrität sind [hier](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenqualit%C3%A4t-und-Datenintegrit%C3%A4t) auffindbar
* Wie die Daten der Patienten geschützt werden, ist in der [Datenschutzfolgeabschätztung](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Datenschutzfolgeabsch%C3%A4tzung) nachzulesen.

## Analyse
Die Analyse wurde mithilfe von Pandas in Python durchgeführt. Die Ergebnisse werden mit Seaborn geplottet. Wie die Analyse nachvollzogen werden kann, ist im Abschnitt [Systemumgebung](https://github.com/Fuenfgeld/DMA2022DataProjectA/wiki/Systemumgebung) zu finden.

## Ergebniszusammenfassung
Durch die Analyse erigbt sich, dass prozentual mehr Menschen an COVID-19 sterben, als in unserem Datensatz generell geimpft sind. In der folgenden Grafik, ist die Verteilung der gegen Influenza geimpften Patienten zu den nicht gegen Influenza Patienten im Datensatz sichtbar
![Kuchendiagramm alle Patienten, 99% geimpfte, 1% ungeimpfte (Bezogen auf die Influenza Impfung)](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/ungeimpft_geimpft_alle.png)

In der zweiten Grafik wird deutlich, dass 19% der an Corona gestorbenen Patienten nicht gegen Influenza geimpft wurden.
![Kuchendiagramm gestorbene Patienten, 81% geimpfte, 19% ungeimpfte (Bezogen auf die Influenza Impfung)](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/ungeimpft_geimpft_gestorben.png)

ufgrund mangelnder Daten können wir jedoch nicht bestätigen, dass ein Zusammenhang herrscht. Beispielweise könnnten auch Menschen, die sich nicht gegen Influenza impfen lassen auch eher nicht gegen COVID-19 impfen lassen. 

Betrachtet man die verschiedenen Ethnien, so lässt sich feststellen, dass die Bevölkerungsgruppe "Black, nonhispanic" prozentual gesehen stärker betroffen war als andere Gruppen. Die folgenden beiden Grafiken stellen einmal in der erstne Grafik die Verteilung der Ethnien bei allen Patienten und in der zweiten Grafik die Verteilung der Ethnien bei den gestorbenen Patienten dar. 

![Balkendiagramm Ethnien aller Patienten](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/verteilung_ethnien_alle.png)

 
![Balkendiagramm Ethnien aller Patienten](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectA/main/Dokumentation/Bilder_analyse/verteilung_ethnien_gestorben.png)

Besonders auffällig ist, dass die Bevölkerungsgruppe ("asian, hispanic") im Balkendiagramm der Verteilung der Ethnien unter den gestorbenen nicht vertreten ist.

## Grafische Darstellung des Projektes
