#not using click?


""" from search import *

import click
from search import *

from isbnlib import * """
#from isbnlib import meta, ISBNLibException
""" from isbnlib.registry import bibformatters, setdefaultservice

SERVICE = "openl"
setdefaultservice(SERVICE)
isbn = "9781538774229"
book = meta(isbn)
bibtex = bibformatters["bibtex"]

def get_search_results(isbn):
    check_isbn(isbn)
    book = meta(isbn)
    bib = bibtex(meta(isbn))
    print(bib) """
""" print(book)
    print(f"Title: {book.get('Title')}")
    print(f"Authors: {book.get('Authors')}")
    print(f"Publisher: {book.get('Publisher')}")
    print(f"Year: {book.get('Year')}") """

""" def check_isbn(isbn):
    cleaned = clean(isbn)
    if is_isbn13(cleaned):
        return cleaned
    elif is_isbn10(cleaned):
        return cleaned
    else:
        sys.exit("Invalid ISBN") """
        # go back to menu

""" @click.group()
def cli():
    pass

@cli.command("add", isbn)
def add_to_library(add):
    input = "Please enter an ISBN number"

@click.group()
def main():
    pass

@cli.command("menu")
def display_main_menu():
    click.echo("---CLI Library---")
    click.echo("-----------------")
    click.echo("add")
    click.echo("2. View Library")
    click.echo("3. Export Library")
    click.echo("4. Book Lookup") """
    #get_main_menu_option()

""" @main.command()
@main.option('--option', prompt="Please enter option number: ", help="Main menu option number")
def get_main_menu_option(option):
    if int(option) == 1:
        return 1
    elif int(option) == 2:
        print("opt 2")
    elif int(option) == 3:
        print("opt 3")
    elif int(option) == 4:
        print("opt 4")
    else:
        print("Please enter a valid option number.")
        get_main_menu_option(option)

@click.command()
def go_to_option(option):
    pass


@click.command()
def get_isbn():
    isbn = input("Enter an ISBN: ")
    return isbn """
