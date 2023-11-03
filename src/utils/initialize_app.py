'''This module is for creating all tables and adding an admin'''

import shortuuid
import hashlib

from src.database.context_manager import DatabaseConnection
from src.config.queries import Query
from src.database import database_access

def create_admin():
    '''To add admin in the table if non present'''
    with DatabaseConnection('src\\database\\travelmanagementsystem.db') as connection:
        if_admin_exists = database_access.single_data_returning_query(Query.SELECT_ADMIN, ('admin', ))
    print(len(if_admin_exists))
    if len(if_admin_exists) != 0:
        return
    with DatabaseConnection('src\\database\\travelmanagementsystem.db') as connection:
        cursor = connection.cursor()
        user_id = 'A_' + shortuuid.ShortUUID().random(length = 8)
        password = hashlib.md5('admin123'.encode()).hexdigest()
        admin_credentials = (user_id, 'admin123', password, 'admin')
        admin_info = (user_id, 'amaira singh', 9087890987, 'female', 34, 'amaira@gmail.com')
        cursor.execute(Query.INSERT_CREDENTIALS, admin_credentials)
        cursor.execute(Query.INSERT_ADMIN, admin_info)

def create_tables() -> None:
    with DatabaseConnection('src\\database\\travelmanagementsystem.db') as connection:
        '''Creating all tables'''
        cursor = connection.cursor()
        cursor.execute(Query.CREATE_CREDENTIALS)
        cursor.execute(Query.CREATE_ADMIN)
        cursor.execute(Query.CREATE_CUSTOMER)
        cursor.execute(Query.CREATE_PACKAGE)
        cursor.execute(Query.CREATE_ITINERARY)
        cursor.execute(Query.CREATE_BOOKING)
        cursor.execute(Query.CREATE_BOOKING_PACKAGE)
        