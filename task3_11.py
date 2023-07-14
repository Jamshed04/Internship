str = input("Введите строку: ")
d = {}
for chr in str:
    if chr != " ":
        d[chr] = str.count(chr)
print(d)