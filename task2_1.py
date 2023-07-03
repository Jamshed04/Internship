import random
print("1)красный\n2)синий\n3)зеленый\n4)черный\n5)белый")
python_color = random.randint(1, 5)
user_color = int(input("Введите номер выбранного цвета: "))
while user_color != python_color:
    if python_color == 1:
        print("Ой, вы поранились...")
    elif python_color == 2:
        print("Посмотрите наверх")
    elif python_color == 3:
        print("Какое красивое дерево")
    elif python_color == 4:
        print("lives matter")
    elif python_color == 5:
        print("Walter Hartwell")
    user_color = int(input("Попробуйте еще раз: "))
print("Отлично!")
