import string, random, os, time

alphabets = list(string.ascii_letters)
target, current = "helloworld", ""
for _ in target:
    letters = alphabets.copy()
    l = ""
    while l != _:
        l = random.choice(letters)
        letters.remove(l)
        print(current + l)
        time.sleep(0.03)
    current += l