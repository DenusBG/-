# --- 1. МНОЖИНИ ---
print("--- МНОЖИНИ ---")
set_a = {1, 2, 3, "Python"}
set_b = {3, 4, 5, "Java"}

print("Об'єднання:", set_a | set_b)
print("Перетин:", set_a & set_b)

# --- 2. СЛОВНИКИ ---
print("\n--- СЛОВНИКИ ---")
student = {
    "ім'я": "Олександр",
    "курс": 2
}

# Використовуємо кому замість f-рядка, щоб уникнути помилок з лапками
print("Студент:", student["ім'я"])
print("Курс:", student["курс"])

# Додавання
student["спеціальність"] = "КН"
print("Оновлений словник:", student)

# --- 3. СТАТИСТИКА (Пункт 4 завдання) ---
text = "apple banana apple"
words = text.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("\nСтатистика:", counts)