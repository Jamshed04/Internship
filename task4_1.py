num = input("Введите  число: ")
max_num = ""
for i in range(len(num)):
    max_num += max(num)
    num = num.replace(max(num), "", 1)
print(max_num)
