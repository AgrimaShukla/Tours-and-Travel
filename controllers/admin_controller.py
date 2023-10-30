''' This module is for admin to create and delete packages '''
import shortuuid 
from tabulate import tabulate 
from utils import validation
from database import query, helper
from config.prompt import CATEGORY_PROMPT, DELETE
class Package:
    def __init__(self, connection):
        try:
            self.connection = connection
            self.package_id = 'P_' + input("Enter ID: ")
            self.package_name = validation.validate_package_name()
            self.duration = validation.validate_duration()
            print(CATEGORY_PROMPT)
            self.category = validation.validate_category()
            self.price = validation.validate_price()
            self.lmt = validation.validate_lmt()
            Package.add_to_package(self)
            print("Successfully added")
        except:
            raise Exception("Error while adding. Try again!!")
 
    def add_to_package(self) -> None:
        data = (self.package_id, self.package_name, self.duration, self.category, self.price, self.lmt)
        helper.add_package(self.connection, query.INSERT_PACKAGE, data)

def show_package(connection) -> None:
    data = helper.show_package_admin(connection)
    row_num = [i for i in range(1, len(data)+1)]
    print(
        tabulate(
        data,
        headers = ["PACKAGE_ID", "PACKAGE_NAME", "DURATION", "PRICE", "LIMIT"],
        showindex = row_num,
        tablefmt = "simple_grid"
        )
    )
     
def delete_package(connection) -> None:
        show_package(connection)
        package_id = input("Package_id: ")
        query_to_delete = query.DELETE_PACKAGE
        helper.delete_package(connection, query_to_delete, package_id)
        print(DELETE)


class Itinerary:
    def __init__(self, connection, package_id: str) -> None:
        self.connection = connection
        self.itinerary_id = "I_" + shortuuid.ShortUUID().random(length = 8)
        self.package_id = package_id
        self.day = validation.validate_days()
        self.city = validation.validate_city()
        self.desc = validation.validate_desc()
        Itinerary.add_location(self, connection)
        
    def add_location(self, connection):
        data = (self.package_id, self.itinerary_id, self.day, self.city, self.desc)
        query_to_insert = query.INSERT_ITINERARY
        helper.add__itinerary(connection, query_to_insert, data)
        print("Added itinerary")

def show_itinerary(connection) -> None:
    query_to_show = query.SHOW_ITINERARY
    data = helper.show_itineary(connection, query_to_show)
    row_num = [i for i in range(1, len(data)+1)]
    print(
        tabulate(
        data,
        headers = ["PACKAGE_ID", "ITINERARY_ID", "DAY", "CITY", "DESC"],
        showindex = row_num,
        tablefmt = "simple_grid"
        )
    )

def delete_itinerary(connection):
    itinerary_id = input("Itinerary_id: ")
    show_package(connection)
    query_to_delete = query.DELETE_ITINERARY
    helper.delete_package(connection, query_to_delete, itinerary_id)
    print(DELETE)
    