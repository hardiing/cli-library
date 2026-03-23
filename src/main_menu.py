from search import get_isbn, get_search_results
from isbnlib import *
from db import *
import sys

def display_library_menu():
    print("---Library Menu---")
    print("-----------------")
    print("1. Add to Library")
    print("2. Book Lookup")
    print("3. Add to Wishlist")
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
        isbn = get_isbn()
        book = get_search_results(isbn)
        print("---ISBN Lookup Results---")
        print(book)
        search_library(book)
        search_wishlist(book)
        
    elif int(option) == 3:
        isbn = get_isbn()
        book = get_search_results(isbn)
        print("---ISBN Lookup Results---")
        print(book)
        confirm = input("Would you like to add this book to your wishlist? y/n: ").strip().lower()
        if confirm == "y":
            add_to_wishlist(book)
        else:
            display_library_menu()
    elif int(option) == 4:
        sys.exit("Thanks for reading!")
    else:
        print("Please enter a valid option number.")
        get_library_menu_option(option)