num = int(input("Введите число: "))
str_num = str(num)
lenght = len(str_num)
sum = 0
for i in range(lenght):
    sum += int(str_num[i])**lenght
if num == sum:
    print("Число Армстронга")
else:
    print("Не является числом Армстронга")