# task2_analysis.py

import random

# Генеруємо список випадкових чисел (від 1 до 100)
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Наш список чисел: {numbers}")

# 1. Вбудовані функції
print(f"Кількість елементів (len): {len(numbers)}")
print(f"Сума чисел (sum): {sum(numbers)}")
print(f"Найменше число (min): {min(numbers)}")
print(f"Найбільше число (max): {max(numbers)}")

# 2. Спискові включення (List Comprehension)
# Створимо новий список, де будуть тільки парні числа
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Тільки парні числа: {even_numbers}")

# Створимо список квадратів цих чисел
squares = [num**2 for num in even_numbers]
print(f"Квадрати парних чисел: {squares}")