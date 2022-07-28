from itertools import count


# countries_information = {}
# countries_information["Polska"] = ("Warszawa", 37.97)
# countries_information["Niemcy"] = ("Berlin", 83.02)
# countries_information["Slowacja"] = ("Bratyslawa", 5.45)

# def show_country_info(country):
#     country_information = countries_information.get(country)
#     print()
#     print(country)
#     print("--------")
#     print("Stolica: "+ country_information[0])
#     print("Liczba mieszkancow w mln: " + str(country_information[1]))

# for country in countries_information.keys():
    # print(country)

# country = input("Inoformacje o jakim kraju chcesz wyswietlic? ")

# show_country_info(country)

def display_sum(a, b):
    print(a+b) #nie zwraca nic

def calculate_sum(a, b):
    return a + b #zwraca wartosc
 
def print_message(): #nic nie przyjmuje ani nic nie zwraca
    print("Message")

display_sum(2, 3)
sum = calculate_sum(2, 3)
print(sum)

print_message()

