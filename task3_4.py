list = []
len = int(input("Введите длину списка: "))
print("Заполните список")
for i in range(len):
    list.append(int(input()))
new_list = [num ** 2 for num in list]
print("Преобразованный список: ", new_list)

