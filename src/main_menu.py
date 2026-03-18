from search import *
from isbnlib import *

def display_main_menu():
    print("---CLI Library---")
    print("-----------------")
    print("1. Library Menu")
    print("2. Book Lookup")
    print("3. Exit")
    get_main_menu_option()

def get_main_menu_option():
    option = input("Please enter option number: ")
    if int(option) == 1:
        display_library_menu()
    elif int(option) == 2:
        isbn = get_isbn
        get_search_results(isbn)
    elif int(option) == 3:
        print("opt 3")
    elif int(option) == 4:
        print("opt 4")
    elif int(option) == 5:
        return 5
    else:
        print("Please enter a valid option number.")
        get_main_menu_option(option)

""" print(book)
    print(f"Title: {book.get('Title')}")
    print(f"Authors: {book.get('Authors')}")
    print(f"Publisher: {book.get('Publisher')}")
    print(f"Year: {book.get('Year')}") """