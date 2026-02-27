# task8.py

input_file = "example.txt"
filtered_file = "filtered_data.txt"
keyword = "Python"  # Шукаємо рядки, де є це слово

try:
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(filtered_file, 'w', encoding='utf-8') as outfile:
        
        found_lines = 0
        for line in infile:
            # Перевіряємо, чи є ключове слово в цьому рядку
            if keyword in line:
                outfile.write(line)
                found_lines += 1
                
    print(f"Фільтрацію завершено. Знайдено рядків: {found_lines}")
    print(f"Результат збережено у '{filtered_file}'")

except FileNotFoundError:
    print("Вхідний файл не знайдено.")