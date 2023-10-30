''' This module deals with all input validation for the user'''
import re
import logging
from config import prompt

def error_handling(func):
    def wrapper(*args, **kwargs):
        try: 
            matched = func(*args, **kwargs)
            if matched == False:
                raise Exception
        except:
            print("Wrong input! Enter again.")
        finally:
            return matched
    return wrapper
        

@error_handling
def input_validation(regex_exp, value) -> bool:
    matched = re.fullmatch(regex_exp, value)
    if matched != None:
        return True
    return False


def validate_name() -> str:
    while True:
        name  = input("Enter name: ")
        check = input_validation('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', name)
        if check == True:
            return name.lower()
        
def validate_number() -> int:
    while True:
        mobile_no = input("Enter mobile number: ")
        check = input_validation('[6-9][0-9]{9}', mobile_no)
        if check == True:
            return mobile_no
        
def validate_gender() -> str:
    while True:
        gender = input("Enter gender (male/female/other): ").lower()
        check = input_validation('male|female|other', gender)
        if check == True:
            return gender
        
def validate_age() -> int:
    while True:
        age = input("Enter age: ")
        check = input_validation('[1-9][0-9]|10[1-9]', age)
        if check == True:
            return age
        
def validate_email():
    while True:
        email = input("Enter email (Eg: - abc@gmail.com): ")
        check = input_validation('^[a-z0-9]+@[a-z]+\.[a-z]{2,3}', email)
        if check == True:
            return email

def validate_username():
    while True:
        username = input("Enter username: ")
        try: 
            if len(username) > 5:
                return username
            else:
                raise Exception
        except:
            print("Wrong input! Enter again.")

def validate_package_name():
    while True:
        package_name = input("Enter package_name: ")
        check = input_validation('^[a-zA-Z]+', package_name)
        if check == True:
            return package_name
        
def validate_person():
    while True:
        number = input("Enter number of people (10 or less): ")
        check = input_validation('^(10|[1-9])$', number)
        if check == True:
            return number
        
def validate_duration():
    while True:
        duration = input("Enter duration (Eg- 3 days 2 nights): ")
        check = input_validation('^([2-5]\sdays\s[1-4]\snights)$', duration)
        if check == True:
            return duration
        
def validate_category():
    while True:
        category = input("Enter category (existing - luxury, midrange and budget): ")
        check = input_validation('^[a-zA-Z]+', category)
        if check == True:
            return category
        
def validate_price():
    while True: 
        price = int(input("Enter price: "))
        # check = input_validation('^[0-9]+', price)
        # if check == True:
        return price
        
def validate_lmt():
    while True: 
        limit = int(input("Enter limit: "))
        # check = input_validation('^[0-9]+', limit)
        # if check == True:
        return limit

def validate_days():
    while True:
        days = input("Enter days: ")
        check  = input_validation('^[0-9]+', days)
        if check == True:
            return days
        
def validate_city():
    while True:
        city = input("Enter city: ")
        check = input_validation('^[a-zA-Z]+', city)
        if check == True:
            return city
        
def validate_desc():
    while True:
        desc = input("Enter desc: ")
        check = input_validation('^[a-zA-Z]+', desc)
        if check == True:
            return desc
