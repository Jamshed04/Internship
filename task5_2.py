import csv

count = int(input("Скоько записей хотите добавить? "))
records = []
for i in range(count):
    book = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    year = input("Введите год выпуска: ")
    records.append([book, author, year])

with open("books.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(records)

    s_author = input("Введите автора книги: ")
    with open("books.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        book = []
        for row in reader:
            if row[1] == s_author:
                book.append(row[0])

    if book:
        print("Книга автора", s_author + ":", ",".join(book))
    else:
        print("Нет книг автора", s_author)