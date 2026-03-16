def display_main_menu():
    print("---CLI Library---")
    print("-----------------")
    print("1. Add to Library")
    print("2. View Library")
    print("3. Export Library")
    print("4. Book Lookup")
    print("5. Exit")
    get_main_menu_option()

def get_main_menu_option():
    option = input("Please enter option number: ")
    if int(option) == 1:
        return 1
    elif int(option) == 2:
        print("opt 2")
    elif int(option) == 3:
        print("opt 3")
    elif int(option) == 4:
        print("opt 4")
    elif int(option) == 5:
        return 5
    else:
        print("Please enter a valid option number.")
        get_main_menu_option(option)