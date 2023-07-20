d = {}
for i in range(1, 11):
    nums = bin(i)
    d[i] = nums[2:]
print("Двоичная запись чисел от 1 до 10: ", d)
