# while True:
#     a=int(input(""))
#     if a % 2 == 0:
#         print("Parzysta")
#     else:
#         print("Nieparzysta")

# tekst = "tekst tekst2 tekst3"
# print(tekst.split(" "))

# join_string=" "
# lista=['Slowo1', 'tekst', 'slowo3']
# print(join_string.join(lista))


# number = int(input("Podaj liczbe uczestników: "))
# i = 0
# lista = []
# while (i<number):
#     imie = input("Wpisz imię: ")
#     lista.append(imie)
#     i+=1
# # print(lista)
# join_string="\n"
# print("Lista uczestników: \n"+join_string.join(lista) )

# def parzysta(liczba):
#     if(liczba % 2 == 0): 
#         print("PARZYSTA!!!")
#     else: 
#         print("NIEPARZYSTA!!!") 

# while True:
#     try:
#         liczba = int(input("Podaj liczbę: "))
#         parzysta(liczba)
#     except ValueError:
#         print("Zła wartość!")

import random


number = random.randint(0,100)
if (number % 2 == 0):
    print("PARZYSTA")
else:
    print("NIEPARZYSTA")
print(number)