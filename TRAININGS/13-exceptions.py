from typing import final


countries_and_capitals = {"Polska": "Warszawa", "Czechy":"Praga", "Niemcy":"Berlin"}

try: #nie przerywa dzialania programu, wyswietla informacje
    print(2/0)
    print(countries_and_capitals["USA"])
except KeyError: #oznaczenie jakiego typu wyjatku szukamy
    print("Klucz nie zostal znaleziony")
except ZeroDivisionError:
    print("Nie dziel przez 0")
finally: #wykona sie niezaleznie od try-except
    print("Jestem zawsze")

print("Jestem tutaj")