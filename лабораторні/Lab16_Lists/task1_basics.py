# task1_basics.py

# 1. Створення
my_list = ["Apple", "Samsung", "Xiaomi", "Motorola"]
my_tuple = ("Windows", "MacOS", "Linux")

print(f"Початковий список: {my_list}")
print(f"Початковий кортеж: {my_tuple}")

# 2. Зміна списку (Mutable)
my_list.append("Nokia")      # Додали в кінець
my_list[1] = "Pixel"         # Замінили Samsung на Pixel
del my_list[0]               # Видалили Apple
print(f"Змінений список: {my_list}")

# Спроба змінити кортеж (викличе помилку, якщо розкоментувати)
# my_tuple[0] = "Android"  # Error! Кортежі незмінні.

# 3. Індекси та Зрізи (Slicing)
print("\n--- Робота зі зрізами ---")
print(f"Перший елемент списку: {my_list[0]}")
print(f"Останній елемент кортежу: {my_tuple[-1]}")
print(f"Перші два телефони: {my_list[0:2]}")
print(f"Список у зворотному порядку: {my_list[::-1]}")