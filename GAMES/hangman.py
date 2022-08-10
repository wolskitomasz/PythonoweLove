import sys
import random


num_of_tries = 5
# word = "tomek"
word = random.choice(open('hangman_words.txt').read().split()).strip() # losowanie slowa (linii ze slowem) do gry z pliku tekstowego
                                                                        # .split() - tworzenie listy ze stringa
                                                                        # .strip() - usuwanie znakow (domyslnie spacji)
user_word = []

used_letters = []

def find_indexess(word, letter):
    indexess = []

    for index, letter_in_word in enumerate(word): # sprawdzenie czy litera podana jest taka sama jak litera w slowie na danym miejscu (indexie)
        if letter == letter_in_word:
            indexess.append(index)
    
    return indexess

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostalo prob:", num_of_tries)
    print("Uzyte litery:", used_letters)
    print()

for _ in word:
    user_word.append("_")     

while True:
    letter = input("Podaj litere: ")
    if letter.isalpha() and len(letter) == 1 and len(letter)>0: # sprawdzanie czy wpisany znak jest litera i czy to jeden znak
        for letter_in_used_letters in used_letters: # przeszukiwanie w zbiorze czy litera sie powtarza
            if letter_in_used_letters==letter:
                print("Uzyles juz tej litery! Uzyj innej!")
                letter = input("Podaj litere: ")
            else:
                continue    
        used_letters.append(letter.lower()) # dodwanie litery do listy
        found_indexess = find_indexess(word, letter) # zmienna przechowujaca indeksy wyciagniete z funkcji szukajacej indeksu w slowie
        
        if len(found_indexess) == 0:
            print("Nie ma takiej litery!")
            num_of_tries-=1

            if num_of_tries == 0:
                print("Koniec gry!")
                sys.exit(0) # zakonczenie programu

        else:
            for index in found_indexess:
                user_word[index] = letter # podmiana podkreslen na litery w slowie

            if "".join(user_word) == word: # laczenie podanych liter do listy w pelne slowo
                print()
                print("Brawo, zgadles!")
                print("Szukanym slowem bylo:", word)
                print()
                sys.exit(0)

        show_state_of_game()
        continue
    else:
        print("To nie litera! Wpisz litere!")    


# dodac:
# sprawdzic czy losowane slowo juz sie w grze pojawilo
# pytanie czy grac dalej/resetowac czy przerwac gre
# pytanie o liczbe prob / stworzenie poziomow trudnosci


# Jest:
# -zamiana wszystkich liter na male litery
# -sprawdzanie czy zostala wpisana litera
# -sprawdzanie czy zostala wpisana pojedynczo
# -sprawdzanie czy podana niepoprawnie litera juz byla podawana
# -sprawdzanie czy poprawnie podana litera zostala juz wykorzystana
# -losowanie slowa do odgadniecia z pliku tekstowego