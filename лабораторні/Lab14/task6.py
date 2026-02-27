# task6.py

source_file = "example.txt"          # Де шукаємо
output_file = "replaced_text.txt"    # Куди записуємо результат
search_word = "Python"               # Що шукаємо (перевірте, чи є це слово в example.txt)
replace_word = "PROGRAMMING"         # На що міняємо

try:
    with open(source_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Виконуємо заміну (створюємо нову змінну з оновленим текстом)
    new_content = content.replace(search_word, replace_word)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
    print(f"Готово! Слово '{search_word}' замінено на '{replace_word}'.")
    print(f"Результат у файлі: {output_file}")

except FileNotFoundError:
    print(f"Файл '{source_file}' не знайдено.")