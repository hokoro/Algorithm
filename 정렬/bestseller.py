t = int(input())

books = [input() for _ in range(t)]

books_set = list(set(books))

books_count = []
for book in books_set:
    books_count.append([book, books.count(book)])

books_count.sort(key=lambda x: (-x[1], x[0]))

print(books_count[0][0])
