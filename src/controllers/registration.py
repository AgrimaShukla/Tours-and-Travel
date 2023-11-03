''' This module is for registering user'''

import hashlib
import logging
import shortuuid

from src.config.queries import Query
from src.utils import validation
from src.config.prompt import PrintPrompts
from src.database.database_access import insert_table

logger = logging.getLogger('__name__')

class Registration:
    '''Registering the customer'''
    def __init__(self) -> None:
        while True:
            print(PrintPrompts.USERNAME_PROMPT)
            self.username = validation.validate_username()
            print(PrintPrompts.PASSWORD)
            self.password = validation.validate_password().encode()
            self.password = hashlib.md5(self.password).hexdigest()
            self.user_id = "U" + shortuuid.ShortUUID().random(length = 10)
            self.name = validation.validate_name()
            self.mobile_no = validation.validate_mobile_number()
            self.gender = validation.validate_gender()
            self.age = validation.validate_age()
            self.email = validation.validate_email()
            self.save_customer()
            break

    def save_customer(self) -> None:
        '''Saving the customer'''
        insert_customer_query = Query.INSERT_CUSTOMER
        insert_credentials_query = Query.INSERT_CREDENTIALS
        customer_credentials = (self.user_id, self.username, self.password, 'user')
        customer_data = (self.user_id, self.name, self.mobile_no, self.gender, self.age, self.email)
        insert_table(insert_credentials_query, customer_credentials, insert_customer_query, customer_data, PrintPrompts.SUCCESFULLY)
