import random
counter = 0
while counter != 3:
    user_num = int(input("Орел(0) или решка(1): "))
    python_num = random.randint(0, 1)
    if not (0 <= user_num <= 1):
        break
    elif user_num  == python_num:
        print("Вы выиграли!")
        counter = 0
    elif user_num != python_num:
        print("Вы проиграли(")
        counter += 1
print("Игра завершена")