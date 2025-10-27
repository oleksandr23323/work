print("'Introduction to programming', Лабораторна 4.1")
print("Kucherenko Oleksandr, FB-51, 15")
import math
epsilon = 0.0001
while True:
    try:
        a = float(input("Введіть додатне число (a): "))
        if a >= 0:
            break
        else:
            print("Введіть додатне число.")
    except ValueError:
        print("Помилка! Введіть, будь ласка, число.")
x_n = a / 2.0
x_prev = 0.0
iter_count = 0
while True:
    iter_count += 1
    x_prev = x_n
    x_n_plus_1 = 0.5 * (x_n + a / x_n)
    x_n = x_n_plus_1
    difference = abs(x_n - x_prev)
    if difference < epsilon:
        break

print("\n--- Результат ---")
print(f"Обчислений квадратний корінь (√{a}) ≈ {x_n}")
print(f"Кількість ітерацій: {iter_count}")
print(f"Перевірка функцією math.sqrt(): {math.sqrt(a)}")