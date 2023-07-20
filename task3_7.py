user_string = input("Введите строку на английскийском: ")
vowels = "aeiouy"
d = {}
for chr in user_string:
    if chr in vowels:
        d[chr] = True
    else:
        d[chr] = False
print(d)
