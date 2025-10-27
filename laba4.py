print("'Introduction to programming', Лабораторна 4.1")
print("Kucherenko Oleksandr, FB-51, 15")
import math
epsilon = 10**-4
S = 0.0
n = 1
a_n = 1

while a_n >= epsilon:
    a_n = math.exp(n) / (100**(n**2)) 
    S += a_n
    n += 1
print(f"Сума ряду S: {S}")