# task2_functions.py

# Функція, яка нічого не повертає, просто вітається
def greet_user(name):
    print(f"Привіт, {name}! Гарного кодування.")

# Функція, яка повертає результат (площа прямокутника)
def calculate_area(width, height):
    area = width * height
    return area

# Виклик функцій
greet_user("Студент")

w = 5
h = 10
result = calculate_area(w, h)
print(f"Площа прямокутника ({w}x{h}): {result}")