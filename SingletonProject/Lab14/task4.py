# task4.py
target_file = "example.txt"

try:
    with open(target_file, 'r', encoding='utf-8') as file:
        # Зчитуємо весь вміст файлу в одну змінну-рядок
        content = file.read()
        
        # 1. Кількість символів (довжина всього тексту)
        num_chars = len(content)
        
        # 2. Кількість слів
        # content.split() розбиває текст на список слів по пробілах та переносах
        words = content.split()
        num_words = len(words)
        
        # 3. Кількість рядків
        # content.splitlines() розбиває текст на список рядків
        lines = content.splitlines()
        num_lines = len(lines)
        
        print(f"--- Статистика файлу '{target_file}' ---")
        print(f"Кількість рядків: {num_lines}")
        print(f"Кількість слів:   {num_words}")
        print(f"Кількість символів: {num_chars}")

except FileNotFoundError:
    print("Файл не знайдено. Створіть 'example.txt' перед запуску!")