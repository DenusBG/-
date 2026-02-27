# task3_program.py

def calculate_average(grades):
    """Функція приймає список оцінок і повертає середнє значення"""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    print("=== Калькулятор середнього балу ===")
    user_grades = []

    while True:
        # Введення даних (Завдання 6)
        user_input = input("Введіть оцінку (або 'stop' для завершення): ")
        
        if user_input.lower() == 'stop':
            break # Вихід з циклу
        
        # Перевірка, чи ввів користувач число
        if user_input.isdigit():
            grade = int(user_input)
            user_grades.append(grade) # Додавання в список
        else:
            print("Будь ласка, введіть число!")

    # Використання функції
    if user_grades:
        avg = calculate_average(user_grades)
        print(f"\nВаші оцінки: {user_grades}")
        print(f"Середній бал: {avg:.2f}") # .2f означає 2 знаки після коми
    else:
        print("Ви не ввели жодної оцінки.")

# Запуск програми
if __name__ == "__main__":
    main()