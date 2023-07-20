from math import sqrt
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
D = sqrt(b ** 2 - 4 * a * c)
if D < 0:
    print("Нет корней")
elif D == 0:
    print("Корень уравнения: ", - b / (2 * a))
elif D > 0:
    print("Корни уравнения: ", (- b + D) / (2 * a), " ", (- b - D) / (2 * a))
