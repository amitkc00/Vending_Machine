import sqlite3
from Exception import Error

class vendingDB:
    database_location = './vendor_database'

    ITEM_TABLE_NAME='ITEMS'
    SALES_TABLE = 'SALES_REPORT'

    def __init__(self):
        try:
            self.conn = sqlite3.connect(database_location)
            #return self.db
        except Error as err:
            print("Error : Failed to initialize Database : {0}".format(err.message))

    @classmethod
    def executeQuery(cls, sql_query, sql_args, get=False):
        """The Primary job of this method is to execute Database Queries sent to it. 
        Open DB, Run Query, Close DB Connection. Handle any exception and pass it along to calling mehtod"""
        
        connection = None

        try:
            connection = sqlite3.connect(cls.database_location)
        except Error as err:
            print("Failed to create database connection {0}".format(err))
            exit(1)
        
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query, sql_args)
            connection.commit()
        except sqlite3.OperationalError as err :
            print('Failed to execute query to database.')
            print(err)
            return(1)
        

    def push(self,name,price,quantity):

        sql_push_item = """ INSERT INTO ITEMS (name, price, quantity) values(?,?,?);"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_push_item, (name, price, quantity))
            self.conn.commit()
        except sqlite3.OperationalError as err :
            print('Failed to push item to database.')
            print(err)


    def getAll(self):
        sql_get_all_items = """ SELECT * FROM ITEMS;"""

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_get_all_items)
            #self.conn.commit()
        except:
            print('Failed to getAll item to database.')


    def update(self,name, priceChange=0, quantityChange=0):

        sql_select_cmd = """ SELECT * from ITEMS where name = ?"""

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_select_cmd, name)
            itemData = conn.fetchone()
        except:
            print('Failed to select')

        newPrice = priceChange
        newQuantity = quantityChange

        sql_update_item = """ UPDATE ITEMS set price=?, quantity=? where name=?"""

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_update_item, (name, newPrice, newQuantity))
            self.conn.commit()
        except :
            print('Failed to update item to database.')


    def createTables(self):

        sql_create_item_table = """CREATE TABLE IF NOT EXISTS ITEMS (id integer PRIMARY KEY,
                                                                     name text NOT NULL,
                                                                     price integer NOT NULL,
                                                                     quantity integer NOT NULL); """


        sql_create_sales_table = """ CREATE TABLE IF NOT EXIST ITEMS (id integer PRIMARY KEY,
                                                                      itemId integer,
                                                                      salePrice integer,
                                                                      saleDate DATE )"""

        try:
            cursor = self.conn.cursor()




            cursor.execute(sql_create_item_table)
            self.conn.commit()

            cursor.execute(sql_create_sales_table)
            self.conn.commit()

        except OperationalError as err:
            print('Failed to create Items Table.')
            print(err)

    def dropTables(self):

        sql_get_all_items = """ SELECT * FROM ITEMS;"""
        sql_drop_items_cmd = """ DROP TABLE ITEMS;"""
        sql_drop_sales_cmd = """ DROP TABLE SALES;"""

        try:

            self.conn = sqlite3.connect(vendingDB.database_location)  
            cursor = self.conn.cursor()
            cursor.execute(sql_get_all_items)
            itemData = cursor.fetchone()

            #Delete tables only if they are not empty.
            if len(itemData) != 0:
                #cursor = self.conn.cursor()
                cursor.execute(sql_drop_items_cmd)
                cursor.execute(sql_drop_sales_cmd)
                self.conn.commit()

        except Error as err:
            print('Failed to drop Tables.')
            print(err)


    def getItemData(self,itemId):

        sql_cmd = """SELECT * FROM ITEMS where id=?"""

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_cmd,(itemId,)) #If you just use name, it is interpreted as len(name) != 1 as you expect.
            itemData = cursor.fetchone()
            return itemData
        except Error as err:
            print('Failed to get Item details from Items Table.')
            print(err)
            # Question :