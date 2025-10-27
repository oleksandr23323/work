print("'Introduction to programming', Лабораторна 4.1")
print("Kucherenko Oleksandr, FB-51, 15")
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    number = abs(n)
    while number > 0:
        count += 1
        number //= 10
    return count
try:
    number_input = int(input("Введіть ціле число: "))
    result = count_digits(number_input)
    print(f"Кількість цифр: {result}")

except ValueError:
    print("Помилка: Необхідно ввести коректне ціле число.")