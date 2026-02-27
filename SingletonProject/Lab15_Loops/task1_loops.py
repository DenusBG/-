# task1_loops.py

# 1. Цикл FOR: Перебір списку
fruits = ["Яблуко", "Банан", "Вишня", "Манго"]
print("--- Перебір списку фруктів ---")
for fruit in fruits:
    print(f"Я люблю {fruit}")

# 2. Цикл FOR: Робота з рядком
word = "Python"
print("\n--- Перебір літер у слові ---")
for letter in word:
    print(letter.upper(), end="-") # end="-" щоб не переносити рядок
print() # Просто пустий print для переносу рядка

# 3. Цикл WHILE: Лічильник
print("\n--- Зворотний відлік ---")
count = 5
while count > 0:
    print(count)
    count -= 1 # Зменшуємо на 1
print("Поїхали!")