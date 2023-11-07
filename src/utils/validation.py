''' This module deals with all input validation for the user'''
import re
import logging
import maskpass

logger = logging.getLogger(__name__)

def error_handling(func):
    '''Decorator for handling errors'''
    def wrapper(*args, **kwargs):
        try: 
            res = func(*args, **kwargs)
            if res == False:
                raise Exception
        except:
            logger.exception("not validated")
            print("Wrong input! Enter again.")
        finally:
            return res
    return wrapper
        

@error_handling
def input_validation(regex_exp: str, value: str) -> bool:
    '''matching regex with value'''
    result = re.fullmatch(regex_exp, value)
    if result != None:
        return True
    return False

def validate(prompts: str, regular_exp: str) -> str:
    '''taking input and pass to input validation'''
    while True:
        value = input(prompts).lower()
        result = input_validation(regular_exp, value)
        if result == True:
            return value
        
def validate_password(regex_exp: str) -> str:
    '''validating password should be minimum of length'''
    while True:
        password = maskpass.advpass()
        result = input_validation(regex_exp, password)
        if result == True:
            return password
        