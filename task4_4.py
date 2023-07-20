from itertools import combinations

num = int(input("Enter target bumber: "))
numbers = [1, 2, 3, 4, 5]
unique_com = []
suitable_comb = []

for i in range(1, len(numbers) + 1):
    comb = list(map(list, combinations(numbers, i)))
    unique_com.extend(comb)

for comb in unique_com:
    if sum(comb) == num:
        suitable_comb.append(comb)
print('Уникальные комбинации: ', suitable_comb)
