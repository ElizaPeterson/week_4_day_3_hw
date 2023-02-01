import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Frank", "Herbert")
author_repository.save(author1)
author2 = Author("J. R. R.", "Tolkien")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Dune", "Sci-fi", "A book about drugs.", author1)
book_repository.save(book1)

book2 = Book("Lord of the Rings: The Fellowship of the Ring", "Fantasy", "A book about a ring.", author2)
book_repository.save(book2)

pdb.set_trace()