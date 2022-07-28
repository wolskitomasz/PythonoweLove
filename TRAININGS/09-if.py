light = input("Jakie jest swiatlo? (red, green, yellow) ")

# if str(light).startswith("r"):
#     print("Czekaj")
# elif light == 'yellow':
#     print("Przygotuj sie")
# elif light == 'green':
#     print("Jedz!")
# else:
#     print("Niewlasciwa wartosc")

print("Jedz!") if light == 'green' else print("Czekaj!") #skrocona forma, dziala tylko przy 2 mozliwosciach