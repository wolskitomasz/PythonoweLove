import sys
import random
import string

password=[]

characters_left = -1

password_length = int(input("Jak dlugie ma byc haslo? "))

def update_characters_left(number_of_characters):
    global characters_left # zeby korzystal z zmiennej globalnej a nie tej w funkcji
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znakow spoza przedzialu 0,", characters_left)
        sys.exit(0) # koniec programu
    else:
        characters_left -= number_of_characters
        print("Pozostalo znakow:", characters_left)

if password_length < 5:
    print("Haslo musi miec minimum 5 znakow!")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("Ile malych liter ma miec haslo? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile duzych liter ma miec haslo? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znakow specjalnych ma miec haslo? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma miec haslo? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostaly wykorzystane, haslo zostanie uzupelnione malymi literami!")
    lowercase_letters += characters_left

print()
print("Dlugosc hasla:", password_length)
print("Male litery:", lowercase_letters)
print("Duze litery:", uppercase_letters)
print("Znaki specjalnie:", special_characters)
print("Cyfry:",digits)

for _ in range(password_length):

    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase)) # generowanie losowej malej litery
        lowercase_letters -= 1

    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1

    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1

    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
       
random.shuffle(password) # wymieszanie listy
print("Wyegenerowane haslo:","".join(password)) # scalenie listy w slowo

# dodac: 
# sprawdzanie czy uzytkownik podaje pojedyncza liczbe
# zamiast konczyc program przy zlej wartosci poprosic o podanie wlasciwej

