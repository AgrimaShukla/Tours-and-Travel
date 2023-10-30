from config.prompt import ADMIN_PROMPT, INVALID_PROMPT, ITINERARY_PROMPT
from controllers.admin_controller import Package, show_package, delete_package, Itinerary, show_itinerary, delete_itinerary
def admin_menu(connection):
    while True:
        print(ADMIN_PROMPT)
        parameter = input("Enter: ")
        match parameter:
            case '1': Package(connection)
            case '2': delete_package(connection)
            case '3': show_package(connection)
            case '4': 
                while True:
                    print(ITINERARY_PROMPT)
                    parameter = input("Enter: ")
                    match parameter:
                        case '1': Itinerary(connection)
                        case '2': show_itinerary(connection)
                        case '3': delete_itinerary(connection)
                        case '4': break
                        case _: print(INVALID_PROMPT)
            case '5': pass
            case '6': break
            case _: print(INVALID_PROMPT)
