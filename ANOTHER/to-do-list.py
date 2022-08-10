tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index) + "]")
        task_index+=1

def add_task():
    task = input("Wpisz tresc zadania: ")
    tasks.append(task) 
    print("Dodano zadanie!")

def delete_task():
    task_index = int(input("Podaj indeks zadania do usuniecia: "))
    if task_index < 0 or task_index > len(tasks) -1:
        print("Zadanie o tym indeksie nie istnieje!")
        return
    tasks.pop(task_index)
    print("Usunieto zadanie!")

def save_tasks_to_file():
    file = open(str(name) +".txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks_from_file():
    # name = input ("Nazwa pliku z danymi: ")
    try:
        file = open(str(name) + ".txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        file = open(str(name) + ".txt", "w+")

def show_menu():
    print()     
    print("1. Pokaz zadania")
    print("2. Dodaj zadanie")
    print("3. Usun zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdz")
    print()

name = input ("Nazwa pliku z danymi: ")
load_tasks_from_file()

user_choice=0

show_menu()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()
        show_menu()
    if user_choice ==2:
        add_task()
        show_menu()
    if user_choice == 3:
        delete_task()
        show_menu()
    if user_choice == 4:
        save_tasks_to_file()
        show_menu()
    
    user_choice = int(input("Wybierz liczbe: "))

    if user_choice < 1 or user_choice > 5 :
        print("Nie ma takiej opcji! Wybierz inna liczbe!")
        show_menu()
        user_choice = int(input("Wybierz liczbe: "))
    else:
        continue

save_tasks_to_file()

# dodac: 
# -dodac opcje zadan wykonanych/trwajacych
# -podzial zadan na kategorie

# Jest:
# sprawdzanie czy liczba jest z zakresu 1-5
# pytanie o nazwe pliku do wczytania / utworzenia
# autozapis po wyjsciu z programu
# sprawdzanie czy zadanie do usuniecia o danym indexie istnieje