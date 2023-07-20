import csv

data = [
    ["Книга", "Автор", "Год выпуска"],
    ["The Headless Horseman", "Mayne Reid", "1866"],
    ["An American Tragedy", "Theodore Dreiser", "1925"],
    ["Martin Eden", "Jack London", "1909"],
    ["White Fang", "Jack London", "1906"]
]

filename = "books.csv"
with open("books.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Файл создан: ", "books.csv")