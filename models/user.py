from config.prompt import DAY_PROMPT, DESTINATION_PROMPT, CATEGORY_PROMPT, INVALID_PROMPT
from controllers.customer_controller import package

def day_menu(connection, dest_option: str, category_option: str) -> None:
    while True:
        print(DAY_PROMPT)
        option = input("Enter: ")
        if option in ['1', '2', '3']:
            package.view_package(connection, dest_option, category_option, option)
        elif option == '4':
            break
        else:
            print(INVALID_PROMPT)

def category_menu(connection, dest_option: str) -> None:
    while True:
        print(CATEGORY_PROMPT)
        option = input("Enter: ")
        if option in ['1', '2', '3']:
            day_menu(connection, dest_option, option)
        elif option == '4':
            break
        else:
            print(INVALID_PROMPT)

def destination_menu(connection) -> None:
    while True:
        print(DESTINATION_PROMPT)
        option = input("Enter: ")
        if option in ['1', '2', '3', '4', '5']:
            category_menu(connection, option)
        elif option == '6':
            break
        else:
            print(INVALID_PROMPT)