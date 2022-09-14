from ast import IsNot, Not
import pandas as pd
from pyparsing import col

#ścieżka do pliku, który czytam
path = "E:/Wiktor/xml-csv/naprawa secz/catalog_product_20220823_115318.csv"
data = pd.read_csv(path,
    low_memory=False)

def removeHeaders(toLeave):
    #colNamestoNOTdel - nazwy kolumn, które nie zostają usunięte
    colNamestoNOTdel = toLeave

    #nazwy kolumn do usunięcia
    colNamesToDel = []

    #każdą nazwę kolumny, która nie jest w liście NIE DO USUNIĘCIA dodaj do listy KOLUMNY DO USUNIĘCIA 
    for colName in data.head():
        if colName not in colNamestoNOTdel:
            colNamesToDel.append(colName)
    #Usuń każdą kolumnę, która jest w liście KOLUMNY DO USUNIĘCIA
    for colName in data.head():
        
        if colName in colNamesToDel:
            data.drop((colName), inplace=True, axis=1)
#Usuń rzędy (wartości do usunięcia, kolumna, która będzie filtrowana)
def removeRows(toRemove,columnToFiltr):

    #lista z indexami do usunięcia
    indexes = []
    #wyciąga nazwy rzędów z pliku, które znajdują się w kolumnie KOLUMNA DO FILTROWANIA, które są w liście DO USUNIĘCIA i pobiera ich indexy
    indexNames = data[data[columnToFiltr].isin(toRemove)].index
    #każdy index, który jest w NAZWY INDEXÓW dodaje do listy INDEXY
    for i in indexNames:
        indexes.append(i)
    #Jeśli podany index jest w liście INDEXY to go usuwa z pliku
        if i in indexes:
            data.drop(i,axis=0,inplace=True)

def leaveRows(toRemove,columnToFiltr):

    
    #wyciąga nazwy rzędów z pliku, które znajdują się w kolumnie KOLUMNA DO FILTROWANIA, które są w liście DO USUNIĘCIA i pobiera ich indexy
    indexNames = [data[-data[columnToFiltr].isin(toRemove)].index]
    #każdy index, który jest w NAZWY INDEXÓW dodaje do listy INDEXY
    for i in indexNames:
        data.drop(i,axis=0,inplace=True)
    

#zapisz do pliku
def saveCSV(pathToSave):
    data.to_csv(pathToSave, sep=",", decimal=".")

# podaj nagłówki do zostawienia, nazwy
removeHeaders(['sku','name','type','price','status','qty','type','backorders']) 
#[podaj co usunac], z ktorej kolumny

# removeRows(['pl','en','de'],'store_view_code')

# do zostawienia
# leaveRows(['simple'],'type')


#ścieżka zapisu
saveCSV('E:/Wiktor/xml-csv/naprawa secz/gotowe2.csv')