''' This module exceute queries to add, delete, fetch and update the tables'''

from tabulate import tabulate
from database import query

class RegisterPerson:

    def insert_credentials(connection, query_to_insert: str, user_id: str, username: str, password: str) -> None:
        cursor = connection.cursor()
        cursor.execute(query.CREATE_CREDENTIALS)
        cursor.execute(query_to_insert, (user_id, username, password, 'admin'))
        connection.commit()

    def insert_customer(connection, query_to_insert: str, data: tuple) -> None:
        cursor = connection.cursor()
        cursor.execute(query.ENABLE_FOREIGN_KEY)
        cursor.execute(query.CREATE_CUSTOMER)
        cursor.execute(query_to_insert, data)
        connection.commit()
       
    def select_credentials_username(connection, username: str) -> tuple:
        cursor = connection.cursor()
        data = cursor.execute(query.SELECT_CREDENTIALS_USERNAME, (username,)).fetchone()
        return data

    def select_credentials_password(connection, username: str, password: str) -> tuple:
        cursor = connection.cursor()
        data = cursor.execute(query.SELECT_CREDENTIALS_PASSWORD, (username, password)).fetchone()
        return data
    
# DATABASE HELPER FOR PACKAGE

def show_package(connection, dest_option: str, category_option: str, day_option: str) -> None:
    cursor = connection.cursor()
    data = cursor.execute(query.SELECT_ITINERARY, (dest_option, category_option, day_option)).fetchall()
    # complete this

def show_package_admin(connection):
    cursor = connection.cursor()
    data = cursor.execute(query.SELECT_PACKAGE_ADMIN).fetchall()
    return data

def add_package(connection, query_to_insert: str, data: tuple) -> None:
    cursor = connection.cursor()
    print(data)
    cursor.execute(query_to_insert, data)
    print("inserted")

def delete_package(connection, query_to_delete: str,package_id: str) -> None:
    cursor = connection.cursor()
    cursor.execute(query_to_delete, (package_id,))

# DATABASE HELPER FOR ITINERARY
def add__itinerary(connection, query: str, data: tuple) -> None:
    cursor = connection.cursor()
    cursor.execute(query, data) 

def show_itineary(connection, query_to_show: str):
    cursor = connection.cursor()
    cursor.execute(query_to_show, ()).fetchall()

def delete_itinerary(connection, query_to_delete:str, itinerary_id: str):
    cursor = connection.cursor()
    cursor.execute(query_to_delete, (itinerary_id, ))


# DATABASE HELPER FOR BOOKING
def book_customer(connection, data: tuple) -> None:
    cursor = connection.cursor()
    cursor.execute(query.CREATE_BOOKING)
    cursor.execute(query.INSERT_BOOKING, data)
    connection.commit()
