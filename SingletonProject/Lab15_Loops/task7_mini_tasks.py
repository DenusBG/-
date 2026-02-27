# task7_mini_tasks.py

print("--- Генерація 40 результатів ---")

# Завдання 1-10: Квадрати чисел
for i in range(1, 11):
    print(f"Завдання {i}: Квадрат числа {i} = {i**2}")

# Завдання 11-20: Перевірка на парність
for i in range(1, 11):
    status = "Парне" if i % 2 == 0 else "Непарне"
    print(f"Завдання {10+i}: Число {i} є {status}")

# Завдання 21-30: Конвертація в дюйми (функція)
def cm_to_inch(cm):
    return cm / 2.54

for i in range(10, 110, 10): # 10, 20... 100
    res = cm_to_inch(i)
    print(f"Завдання {20 + i//10}: {i} см = {res:.2f} дюймів")

# Завдання 31-40: Робота з текстом
words = ["Python", "Java", "C++", "Go", "Rust", "Swift", "PHP", "Ruby", "Perl", "JS"]
for i, w in enumerate(words):
    print(f"Завдання {31+i}: Довжина слова '{w}' - {len(w)} символів")