import random
import string

num_of_characters = int(input("Ile znakow ma miec haslo? "))

passowrd = "".join(random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(num_of_characters))
print("Wygenerowane haslo:", passowrd)
