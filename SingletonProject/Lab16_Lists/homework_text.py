def analyze_text(text):
    # 1. Розбиваємо текст на список слів
    words = text.lower().replace('.', '').replace(',', '').split()
    
    # 2. Використовуємо set (множину) для пошуку унікальних
    unique_words = sorted(list(set(words)))
    
    # 3. Результат у вигляді кортежу
    return (len(words), len(unique_words), unique_words)

# Текст для аналізу
input_text = "Python це круто. Python це просто. Ми любимо Python."

total, unique, unique_list = analyze_text(input_text)

print(f"Текст: {input_text}")
print(f"Всього слів: {total}")
print(f"Унікальних слів: {unique}")
print(f"Список унікальних: {unique_list}")