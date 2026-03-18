import sys
from isbnlib import *
#from isbnlib import meta, ISBNLibException
from isbnlib.registry import bibformatters, setdefaultservice
#from main_menu import display_main_menu
#from library import get_isbn
from db import *

SERVICE = "openl"
setdefaultservice(SERVICE)
#isbn = "9781538774229"
bibtex = bibformatters["bibtex"]

def display_library_menu():
    print("---Library Menu---")
    print("-----------------")
    print("1. Add to Library")
    print("2. View Library")
    print("3. Export Library")
    print("4. Exit App")
    get_library_menu_option()

def get_library_menu_option():
    option = input("Please enter option number: ")
    if int(option) == 1:
        isbn = get_isbn()
        book = get_search_results(isbn)
        print("---ISBN Lookup Results---")
        print(book)
        confirm = input("Would you like to add this book? y/n: ").strip().lower()
        if confirm == "y":
            add_to_db(book)
        else:
            display_library_menu()
    elif int(option) == 2:
        print("opt 2")
    elif int(option) == 3:
        print("opt 3")
    elif int(option) == 4:
        sys.exit("Thanks for reading!")
    elif int(option) == 5:
        return 5
    else:
        print("Please enter a valid option number.")
        get_library_menu_option(option)

def get_isbn():
    isbn = input("Please enter ISBN number: ").strip()
    return isbn

def get_search_results(isbn):
    check_isbn(isbn)
    try:
        bib = bibtex(meta(isbn))
    except:
        print("ISBN not found in Open Library")
        print("---Returning to Library Menu---\n")
        display_library_menu()
    return bib

def check_isbn(isbn):
    cleaned = clean(isbn)
    if is_isbn13(cleaned):
        return cleaned
    elif is_isbn10(cleaned):
        return cleaned
    else:
        print("Invalid ISBN")
        display_library_menu()