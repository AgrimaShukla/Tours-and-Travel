''' This module is for customer to view and book package'''
from shortuuid import ShortUUID
from datetime import datetime, timedelta
from config.mapping_values import destination_dict, category_dict, day_dict
from utils import validation
from config.prompt import DATE_PROMPT, INVALID_DATE
from database.helper import book_customer
    

class BookPackage:
    def __init__(self, connection, package_id: str, days_night: str) -> None:
        try:
            self.connection = connection
            self.package_id = package_id
            self.booking_id = "B_" + ShortUUID.random(length = 10)
            self.name = validation.validate_name()
            self.mobile_no = validation.validate_number()
            print(DATE_PROMPT)
            date_str = input("Enter: ")
            try:
                self.start_date = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print(INVALID_DATE)
            words = days_night.split()
            day = words[0]
            self.end_date = self.start_date + timedelta(days = day)
            self.number_of_people = validation.validate_person()
            self.email = validation.validate_email()
            self.booking_date = datetime.now()
            data = (self.booking_id, self.name, self.mobile_no, self.start_date, self.end_date, self.number_of_people, self.email, self.booking_date)
            BookPackage.booking(data)
        except:
            raise Exception("Unable to book package. Try again!!")
        
    def booking(self, data: tuple):
        book_customer(self.connection, data)
        print("Booked successfully!")
    
    def delete_booking():
        pass

class package:
    def view_package(destination, category, days_night):
        dest_value = destination_dict[destination]
        category_value = category_dict[category]
        day_value = day_dict[days_night]
        


        
        
    
    