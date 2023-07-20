string = input("Введите строку: ")
for i in range(len(string)):
    if string[i] == string[i].title():
        print(string[i].lower(), end='')
    elif string[i] == string[i].lower():
        print(string[i].title(), end='')
    else:
        print(" ", end='')
