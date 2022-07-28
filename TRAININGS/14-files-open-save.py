# file = open("file.txt") #otwiera plik
# file = open("file.txt", "r") #otwiera plik domyslnie
# file = open("file.txt", "w") #otwiera plik do zapisu
file = open("countries_and_capitals.txt", "w+") #otwiera plik do zapisu i odczytu lub go tworzy

countries_and_capitals = {"Polska": "Warszawa", "Czechy":"Praga", "Niemcy":"Berlin"}

for country, capital in countries_and_capitals.items(): #.items() zeby przeszlo i przez klucze i wartosci a nie tylko klucze
    file.write(country + "-" + capital + "\n")

file.close() #zamyka plik

#odczyt

file = open("countries_and_capitals.txt")
for line in file.readlines(): #odczytywanie linii
    print(line.strip()) #.strip() usuwa niepotrzebne znaki konca linii
    
file.close()