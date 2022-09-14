import os,sys
import random

enteredPath = input("Podaj sciezke: ")
kw = input("wklej slowa kluczowe oddzielone przecinkiem: ").replace(" ", "-")
path = enteredPath.replace("\\","/")


string=kw

listFromString = string.split(",")*30
# print(listFromString)
# print(type(listFromString))

files = os.listdir(path)

i=0
print("powered by Wiktor Ćwiertnia v1.2")
input("wcisnij przynisk zeby zakonczyc")

while i < len(listFromString):
    max = 100
    min = 999

        # index = 0
    for index, file in enumerate(files):
        i = index

        if(i == len(listFromString)):
            i = 0

        kw = listFromString[i]
        print(kw)
        randomNr = str(round((random.random() * (max - min) + min)))
        os.rename(os.path.join(path, file), os.path.join(path, str(index).join([str(kw+randomNr), '.jpg'])))
