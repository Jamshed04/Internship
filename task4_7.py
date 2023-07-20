import itertools

s = input("Введите список: ")
lst = list(s)
permutations = list(itertools.permutations(lst))

print([''.join(permutation) for permutation in permutations])