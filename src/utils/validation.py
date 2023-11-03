''' This module deals with all input validation for the user'''
import re
import logging
import maskpass

logger = logging.getLogger(__name__)

def error_handling(func):
    '''Decorator for handling errors'''
    def wrapper(*args, **kwargs):
        try: 
            matched = func(*args, **kwargs)
            if matched == False:
                raise Exception
        except:
            logger.exception("not validated")
            print("Wrong input! Enter again.")
        finally:
            return matched
    return wrapper
        

@error_handling
def input_validation(regex_exp, value) -> bool:
    '''matching regex with value'''
    matched = re.fullmatch(regex_exp, value)
    if matched != None:
        return True
    return False

def validate_age() -> int:
    '''validating age. Age should be from 10 to 109'''
    while True:
        age = input("Enter age: ")
        check = input_validation('[1-9][0-9]|10[1-9]', age)
        if check == True:
            return age

def validate_duration() -> str:
    '''validating duration x days y nights'''
    while True:
        duration = input("Enter duration (Eg- 3 days 2 nights): ")
        check = input_validation('^([2-5]\sdays\s[1-4]\snights)$', duration)
        if check == True:
            return duration

def validate_email() -> str:
    '''validating email. Eg - agrima@gmail.com'''
    while True:
        email = input("Enter email (Eg: - abc@gmail.com): ")
        check = input_validation('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', email)
        if check == True:
            return email

def validate_gender() -> str:
    '''validating gender (male or female or other)'''
    while True:
        gender = input("Enter gender (male/female/other): ").lower()
        check = input_validation('male|female|other', gender)
        if check == True:
            return gender
             
def validate_mobile_number() -> int:
    '''validating mobile numbers starting from 6 to 9 and of 10 digits'''
    while True:
        mobile_no = input("Enter mobile number: ")
        check = input_validation('[6-9][0-9]{9}', mobile_no)
        if check == True:
            return mobile_no
        
def validate_name() -> str:
    '''validating names'''
    while True:
        name  = input("Enter name: ")
        check = input_validation('^([A-Za-z]{2,25}\s*)+', name)
        if check == True:
            return name.lower()
        
# validate price, limit and days
def validate_number(value: str) -> str:
    '''validating numbers'''
    while True: 
        digits = input(f"Enter {value}: ")
        check = input_validation('^[0-9]+', digits)
        if check == True:
            return digits
        
def validate_password() -> str:
    '''validating password should be minimum of length'''
    while True:
        password = maskpass.advpass()
        check = input_validation('^.{5,20}$', password)
        if check == True:
            return password
        
def validate_person() -> str:
    '''validating number of people should be less than 10'''
    while True:
        number = input("Enter number of people (10 or less): ")
        check = input_validation('^(10|[1-9])$', number)
        if check == True:
            return number

def validate_status() -> str:
    '''validating status should active or in active'''
    while True:
        status = input("Enter status (active/inactive): ").lower()
        check = input_validation('active|inactive', status)
        if check == True:
            return status
        
# validate city, category, description and package name
def validate_string(value: str) -> str:
    '''validating strings'''
    while True:
        string_input = input(f"Enter {value}: ").lower()
        check = input_validation('^([A-Za-z]{2,25}\s*)+', string_input)
        if check == True:
            return string_input
        
def validate_username() -> str:
    '''validating username can contain alphanumeric, underscores and hyphen'''
    while True:
        username = input("Enter username: ")
        check  = input_validation('^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]+$', username)
        if check == True:
            return username