''' Authenticating the user at the time of login '''

import time
import maskpass
import hashlib
import logging
from database.helper import RegisterPerson

logger = logging.getLogger('authentication')

class Authentication:
    ''' class for authenticating user'''
    def __init__(self, connection) -> None:
        self.connection = connection
        self.attempts = 3

    def invalid_username(self) -> None:
        logger.error("Invalid login attempt")
        print("Invalid username! Enter again.")
        self.attempts = self.attempts - 1
    
    def invalid_password(self) -> None:
        logging.error("Invalid login attempt")
        print("Invalid username or password! Enter again")
        self.attempts = self.attempts - 1

    def user_authentication(self) -> tuple:
        while self.attempts > 0: 
            username = input("Enter your username: ")
            password = maskpass.advpass().encode()
            password = hashlib.md5(password).hexdigest()
            try:
                user_data = RegisterPerson.select_credentials_username(self.connection, username)
                if user_data == None:
                    Authentication.invalid_username(self)
                    continue
                elif user_data[0] == password:
                    role = RegisterPerson.select_credentials_password(self.connection, username, password)
                    return role[0]
                else:
                    Authentication.invalid_password(self)
                    continue
            except:
                print("Error encountered")

        print("Attempts exhausted")
        time.sleep(3)
        return


                     


                
                    

                
                
                