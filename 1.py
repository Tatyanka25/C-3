'Zadanie1'
Name, Surname = input("Введите имя и фамилию через пробел: ").split()
Birthday = int(input("Введите год рождения: "))
print(Name, "_", Surname, "_", Birthday)
Name, Surname = Surname, Name # Меняем местами переменные
Birthday = Birthday + 60
print(Name, "_", Surname, "_", Birthday)