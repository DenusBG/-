# task3_methods.py

students = [
    ("Олександр", 85),
    ("Марія", 92),
    ("Дмитро", 78),
    ("Анна", 95)
]

def add_student(name, grade):
    """Додає студента у список"""
    students.append((name, grade))
    print(f"Додано: {name}")

def get_best_student():
    """Знаходить студента з найвищим балом"""
    # Сортуємо список за другим елементом кортежу (оцінкою)
    students.sort(key=lambda x: x[1], reverse=True)
    return students[0]

# Використання
print("--- Список студентів ---")
for s in students:
    print(f"Ім'я: {s[0]}, Бал: {s[1]}")

print("\n--- Додавання нового ---")
add_student("Максим", 88)

best = get_best_student()
print(f"\nНайкращий студент: {best[0]} з балом {best[1]}")