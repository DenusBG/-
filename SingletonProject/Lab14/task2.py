# Завдання 2: Запис у текстовий файл

filename = "user_data.txt"
lines_to_write = []

print("Введіть текст (введіть 'STOP' окремим рядком, щоб завершити):")

while True:
    text = input("> ")
    if text == "STOP":
        break
    lines_to_write.append(text + "\n") # Додаємо перенос рядка

# 'w' означає write (запис). УВАГА: це створить новий файл або перезапише старий!
with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

print(f"Дані успішно записано у файл '{filename}'. Подивіться на панель зліва!")