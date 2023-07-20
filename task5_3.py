import csv

starting_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))

with open('books.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    if starting_year > end_year:
        print("Некоректный запрос;(")
    else:
        print("Книги в данном промежутке:")
        for row in reader:
            year = int(row[2])
            if starting_year <= year <= end_year:
                print(row[0])