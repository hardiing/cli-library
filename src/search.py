import sys
from isbnlib import *
from isbnlib.registry import bibformatters, setdefaultservice
from db import *

SERVICE = "openl"
setdefaultservice(SERVICE)
#isbn = "9781538774229"
#bibtex = bibformatters["bibtex"]
bibjson = bibformatters["json"]

def get_isbn():
    isbn = input("Please enter ISBN number: ").strip()
    return isbn

def get_search_results(isbn):
    check_isbn(isbn)
    try:
        bib = bibjson(meta(isbn, SERVICE))
    except:
        print("ISBN not found in Open Library")
        sys.exit("Thanks for reading!")
    return bib

def check_isbn(isbn):
    cleaned = clean(isbn)
    if is_isbn13(cleaned):
        return cleaned
    elif is_isbn10(cleaned):
        return cleaned
    else:
        print("Invalid ISBN")
        sys.exit("Thanks for reading!")