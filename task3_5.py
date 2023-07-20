num = int(input("Введите число: "))
not_prime = [n for n in range(2, num + 1)
             if any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))]
print("Список не простых чисел: ", not_prime)
