# task4_libs.py
import math
import itertools
import time

# 1. Використання MATH
number = 16
sqrt_val = math.sqrt(number)
factorial_val = math.factorial(5) # 1*2*3*4*5

print(f"Корінь з {number} = {sqrt_val}")
print(f"Факторіал 5 = {factorial_val}")

# 2. Використання ITERTOOLS (Нескінченний цикл, обережно!)
print("\n--- Світлофор (itertools.cycle) ---")
colors = ["Червоний", "Жовтий", "Зелений"]
cycle_colors = itertools.cycle(colors)

# Пройдемося по кольорах 6 разів
for i in range(6):
    current_color = next(cycle_colors)
    print(f"Світлофор: {current_color}")
    # time.sleep(0.5) # Можна розкоментувати для паузи