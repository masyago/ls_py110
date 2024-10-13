books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

# need to sort by values of keys published. sort as int (key=int)

def get_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_year)
print(sorted_books)