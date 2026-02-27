# Завдання 4: IndexError
try:
    список = [1, 2]
    print(список[5])
except IndexError:
    print("Помилка: Індекс поза межами списку!")

# Завдання 5: KeyError
try:
    словник = {"a": 1}
    print(словник["b"])
except KeyError:
    print("Помилка: Такого ключа немає!")