num = int(input("Введите число для проверки: "))
print((lambda n: "Число четное" if n % 2 == 0 else "Число нечетное")(num))
