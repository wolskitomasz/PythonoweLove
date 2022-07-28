# names_list = []
# names_list.append("Tomek")
# names_list.append("Marcin")

# names_list = ["Tomek", "Marcin", "Adam", "Tomek"]

# print(names_list)

# names_list.sort() #sortuje alfabetycznie
# names_list.sort(reverse=True) #sortuje odwrotnie

# names_list.reverse() #odwrocenie listy

# for name in names_list: #dla kazdego obiektu listy
#     print(name)

# print(names_list[0]) #wypisanie danego elementu listy
# print(names_list.count("Tomek")) #liczy ilosc tych samych elementow

#print(len(names_list)) #ilosc elementow

# names_list.remove("Tomek") #usuwa pierwsze wystwapienie danej wartosci

# names_list.clear() #czysci liste

# print(names_list.pop(0)) #wyswietla element i go usuwa z listy
# print(names_list)

# names_list2 = ["Dominik"]

# names_list3 = names_list + names_list2 #laczenie list

# print(names_list3)

# person = ("Tomek", "Wolski", 32) #krotka - struktura niezmienna

# print(len(person))
# print(person.count("Tomek"))

# print(person)

# names_set = {"Kamil", "Mariusz", "Kamil"} #nie moga sie powtarzac elementy, nie sa uporzadkowane, nie maja id

# names_set = set() #tworzenie pustego setu
# names_set.add("Kamil") #dodawanie do setu
# names_set.add("Dominik")

# names_set.remove("Kamil") #usuwanie z setu
# names_set.discard("Adam") #nie wyswietla bledu w momencie gdy danego elementu juz nie ma
# print(names_set)

# for name in names_set:
#     print(name)

# names_list = []
# names_tuple = ()

# names_set.add(names_list) #hie mozna dodac elementow listy do setu
# names_set.add(names_tuple) #mozna dodac elementy krotki do setu

# names_set2 = {"Mariusz", "Tytus", "Kamil"} 

# names_set3 = names_set.union(names_set2) #laczenie ze soba setow, union - zwraca nowy set nie modyfikujac pierwotnego

# names_set.update(names_set2) #dodaje do pierwszego setu elementy z drugiego setu

# names_set3 = names_set.difference(names_set2) #porownanie setow, roznica miedzy setami

# names_set3 = names_set.intersection(names_set2) #czesc wspolna dwoch setow

# names_set3 = names_set.symmetric_difference(names_set2) #elementy spoza czesci wspolnej

# names_set.clear() #czysci set

# names_list = ["Artur", "Rafal"]

# names_list.extend(names_set2) #dodanie do listy elementow z setu

# print(names_list)

# print(names_set3)

countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"} #slownik
countries_and_capitals['Czechy'] = "Praga" #dodanie do slownika

# print(countries_and_capitals)

# for country in countries_and_capitals.keys(): #wypisuje klucz
#     print(country)

# for capital in countries_and_capitals.values(): #wypisuje wartosci
#     print(capital)

# for country, capital in countries_and_capitals.items(): #wypisuje wszystkie elementy
#     print(country + "-" + capital)

# print(countries_and_capitals["Poland"]) #wyswietla wartosc dla klucza, wyrzuca blad gdy klucza nie ma
# print(countries_and_capitals.get("Poland")) #wyswietla wartosc dla klucza, nie wyrzuca bledu, zwraca None gdy nie ma klucza
# print(countries_and_capitals.setdefault("USA", "Washington DC")) #pobiera wartosc danego klucza, jezeli go nie ma tworzy nowy 
                                                                    #klucz i wstawia jemu wartosc / moze tez podmienic wartosc dla danego klucza
# countries_and_capitals.pop("Poland") #usuwa klucz, zwraca blad gdy juz go nie ma

# print(countries_and_capitals.popitem()) #.popitem() usuwa ostatnia dodana wartosc z slownika

# if "Poland" in countries_and_capitals: #przeszukiwanie slownika po kluczach
#     print("znaleziono")
# else:
#     print("nie znaleziono")

countries_and_capitals.clear() #czysci slownik
print(countries_and_capitals)