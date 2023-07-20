num = int(input("Введите число: "))
sum = 0
while num < 0:
    sum += num
    print("Сумма: ", sum)
    num = int(input("Введите еще числа: "))
