score = int(input("Введите количество очков: "))
if score == 3:
    print("Выигрыш")
elif score == 1:
    print("Ничья")
elif score == 0:
    print("Проигрыш")
else:
    print("Error")
