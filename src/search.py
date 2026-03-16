import sys
from isbnlib import *
#from isbnlib import meta, ISBNLibException
from isbnlib.registry import bibformatters, setdefaultservice
from main_menu import display_main_menu

SERVICE = "openl"
setdefaultservice(SERVICE)
isbn = "9781538774229"
book = meta(isbn)
bibtex = bibformatters["bibtex"]

def get_search_results(isbn):
    check_isbn(isbn)
    book = meta(isbn)
    bib = bibtex(meta(isbn))
    print(bib)
    """ print(book)
    print(f"Title: {book.get('Title')}")
    print(f"Authors: {book.get('Authors')}")
    print(f"Publisher: {book.get('Publisher')}")
    print(f"Year: {book.get('Year')}") """

def check_isbn(isbn):
    cleaned = clean(isbn)
    if is_isbn13(cleaned):
        return cleaned
    elif is_isbn10(cleaned):
        return cleaned
    else:
        print("Invalid ISBN")
        display_main_menu()