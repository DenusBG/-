import random

def get_random_number():
    """Генерує число від 1 до 100"""
    return random.randint(1, 100)

def play_game():
    secret_number = get_random_number()
    attempts = 0
    print("🎮 Вітаю у грі 'Вгадай число'!")
    print("Я загадав число від 1 до 100. Спробуй вгадати.")

    while True:
        try:
            user_guess = int(input("Твій варіант: "))
            attempts += 1

            if user_guess < secret_number:
                print("🔽 Замало! Спробуй більше.")
            elif user_guess > secret_number:
                print("🔼 Забагато! Спробуй менше.")
            else:
                print(f"🎉 Вітаю! Ти вгадав число {secret_number} за {attempts} спроб!")
                break # Перемога, вихід з циклу
        except ValueError:
            print("❌ Будь ласка, введи число.")

if __name__ == "__main__":
    play_game()