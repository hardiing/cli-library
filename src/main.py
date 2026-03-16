# library CLI app
# default is isbn lookup (pip install isbnlib)
# click for interface (pip install click)
# manually add fields after
# view library / add to library

import click

from main_menu import *
from search import get_search_results

def main():
    # welcome message
    # 1 add to library
    #   isbn, if not found, manual entry
    # 2 library
    #   search library
    #   view library
    #   export csv?
    # 3 lookup book
    #   add to library?
    # 4 wishlist?
    # 5 exit
    display_main_menu()
    #isbn = get_isbn(standalone_mode=False)
    #get_search_results(str(isbn))
    
if __name__ == "__main__":
    main()
