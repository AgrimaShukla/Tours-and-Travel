''' This module is for registering user'''

import logging
import shortuuid
import maskpass
import hashlib
from database import query
from utils import validation
from database.helper import RegisterPerson

logger = logging.getLogger('registration')

class Registration:
    def __init__(self, connection) -> None:
        self.connection = connection
        try:
            self.username = validation.validate_username()
            self.password = maskpass.advpass().encode()
            self.password = hashlib.md5(self.password).hexdigest()
            self.user_id = "U" + shortuuid.ShortUUID().random(length = 10)
            self.name = validation.validate_name()
            self.mobile_no = validation.validate_number()
            self.gender = validation.validate_gender()
            self.age = validation.validate_age()
            self.email = validation.validate_email()
            Registration.save_credentials(self)
            Registration.save_customer(self)
            print("Successfully registered")
        except:
            raise Exception("Error while registering! Try again")
        
    def save_credentials(self) -> None:
        query_to_insert = query.INSERT_CREDENTIALS
        RegisterPerson.insert_credentials(self.connection, query_to_insert, self.user_id, self.username, self.password)

    def save_customer(self) -> None:
        query_to_insert = query.INSERT_CUSTOMER
        data = (self.user_id, self.name, self.mobile_no, self. gender, self.age, self.email)
        RegisterPerson.insert_customer(self.connection, query_to_insert, data)


