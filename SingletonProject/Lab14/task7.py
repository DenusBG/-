# task7.py
import pickle  # Цей модуль потрібен для бінарного запису об'єктів

filename = "numbers.bin"
data_to_save = [10, 20, 30, 40, 50]  # Наш список чисел

# 1. Запис у бінарний файл ('wb' = write binary)
with open(filename, 'wb') as file:
    pickle.dump(data_to_save, file)
    print("Числа записано у бінарний файл.")

# 2. Читання з бінарного файлу ('rb' = read binary)
with open(filename, 'rb') as file:
    loaded_data = pickle.load(file)
    print(f"Зчитано список: {loaded_data}")

# 3. Обчислення суми
total_sum = sum(loaded_data)
print(f"Сума чисел: {total_sum}")