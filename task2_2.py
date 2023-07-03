shows = ["Галилео", "Мир наизнанку", "Орел и решка", "Вечерний ургант"]
user_show = input("Введите название ТВ передачи: ")
position = int(input("Введите позцию передачи: "))
for i in range(1, len(shows)+1):
    if position == i:
        print(user_show)
    print(shows[i-1])
    if position == 5 and i == 4:
        print(user_show)