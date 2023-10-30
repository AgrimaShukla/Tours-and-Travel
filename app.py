''' Travel Itinerary system
    This module is entry point
'''
import logging
import sqlite3
import sys
from config import prompt
from models import user, admin
from registration import Registration
from utils.authentication import Authentication

logging.basicConfig(format = '%(asctime)s - %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    filename = 'logs.txt',
                    level = logging.DEBUG)
logging.getLogger("main")

connection = sqlite3.connect("toursandtravels.db")

def main(connection) -> None:
    while True:
        print(prompt.NAME)
        print(prompt.ENTRY_PROMPT)
        parameter = input("ENTER: ")
        match parameter:
            case '1': 
                    Registration(connection)
                    obj_authenticate = Authentication(connection)
                    role = obj_authenticate.user_authentication()
                    if role == 'user':
                        user.destination_menu(connection)
                    else:
                        continue
            case '2': 
                    obj_authenticate = Authentication(connection)
                    role = obj_authenticate.user_authentication()
                    if role == 'user':
                        user.destination_menu(connection)
                    elif role == 'admin':
                        admin.admin_menu(connection)
                    else:
                        continue
                    
            case '3': pass
            case _: print(prompt.INVALID_PROMPT)

if __name__ == "__main__":
    main(connection)
    connection.close()

else:
     sys.exit()