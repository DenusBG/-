# task5.py
source_file = "example.txt"      # Звідки беремо
destination_file = "copy_of_example.txt" # Куди кладемо (цей файл створиться сам)

try:
    # Крок 1: Читаємо дані
    with open(source_file, 'r', encoding='utf-8') as src:
        data = src.read()
    
    # Крок 2: Записуємо дані у новий файл
    with open(destination_file, 'w', encoding='utf-8') as dest:
        dest.write(data)
        
    print(f"Файл успішно скопійовано! Створено новий файл: {destination_file}")

except FileNotFoundError:
    print(f"Не можу знайти файл '{source_file}' для копіювання.")