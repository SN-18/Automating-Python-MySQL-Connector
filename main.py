import mysql.connector
import sys

# total arguments
print("--------------------------Start--------------------------------------------------\n")
print("STARTER INFO\n")
print("This program accepts Id, Name, Price, Purchase Date to Insert into Customer Table")
print("It will create an RDBMS using mySQL")
print("The Python Connector API will convey this to SQL")
print("The connector API will then fetch these from the database and display them")
print("This demonstrates a working connection")
print("\n\n")


print("\nName of Python script:", sys.argv[0])


li=[]
for i in range(1,5):
    li.append(sys.argv[i])

id,name,price,purchase_date = li


mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password='',
    database="mydatabase"
)


cursor = mydb.cursor()


try:
    mysql_insert_query = """INSERT INTO CUSTOMERS (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

    record = (id, name, price, purchase_date)

    # preparing a cursor object
    cursorObject = mydb.cursor()
    cursor.execute(mysql_insert_query, record)
    mydb.commit()

    print("Record inserted successfully into CUSTOMERS table via Python Connect API")


    sqlite_select_query = """SELECT * from mydatabase.CUSTOMERS"""
    cursor.execute(sqlite_select_query)

    li=list(cursor.fetchall()[0])
    print("The parameters entered by the user are:")
    print("****************************************\n")

    for i in li:
        print(i)

    print("\n****************************************\n")




except mysql.connector.Error as error:
    st="Failed to insert into MySQL table {}"
    print(st.format(error))

print("The db connection object can be seen here as: , with it's hex location\n")
print(mydb)








#debugging
# Creating a database with a name
# 'geeksforgeeks' execute() method
# is used to compile a SQL statement
# below statement is used to create
# the 'geeksforgeeks' database
# cursor.execute("CREATE DATABASE geeksforgeeks")
# This is a sample Python script.
# import mysql.connector
#
# cnx = mysql.connector.connect(user='saurabhnanda',
#                               host='127.0.0.1',
#                               password='',
#                               database='menagerie')
# cnx.close()
#
# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="yourusername",
# #   password="yourpassword"
# #
# # )
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# if name== "__main__" :


# n = len(sys.argv)
# print("Display User Defined Command Line Arguments\n")
# Arguments passed

# query="CREATE TABLE CUSTOMERS (id VARCHAR(255), name VARCHAR(255), price INT, purchase_date DATE )"
# cursor.execute(query)
# cursor.execute("CREATE DATABASE mydatabase")

# import mysql.connector

# print("\nArguments passed:", end=" ")
# for i in range(1, n):
#     print(sys.argv[i], end=" ")
# print("\n")

# def insert_varibles_into_table(id, name, price, purchase_date):
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='Electronics',
#                                              user='pynative',
#                                              password='pynative@#29')
#         cursor = connection.cursor()
#         mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
#                                 VALUES (%s, %s, %s, %s) """
#
#         record = (id, name, price, purchase_date)
#         cursor.execute(mySql_insert_query, record)
#         connection.commit()
#         print("Record inserted successfully into Laptop table")
#
#     except mysql.connector.Error as error:
#         print("Failed to insert into MySQL table {}".format(error))
#
#     finally:
#         if mydb.is_connected():
#             # cursor.close()
#             # mydb.close()
#             print("MySQL connection is closed")

# id="203"
# name="Name"
# price="480"
# purchase_date="2/03/01"

# print("This would print cursor.fetchall",li)



    #debugging (resolved now)
    # cursor.execute("SELECT CUSTOMERS FROM mydatabase.tables")
    # for table_name in cursor:
    #     print(table_name)

    #end of debugging
    # cursor.execute("SHOW TABLES")
    # print(records)

    # result = cursor.fetchall()

    # print("this should be printed after fetching")

    # print(result)

# creating database
    # cursorObject.execute("CREATE DATABASE geeksforgeeks")

# insert_varibles_into_table(2, 'Area 51M', 6999, '2019-04-14')
# insert_varibles_into_table(3, 'MacBook Pro', 2499, '2019-06-20')
# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
# print("this should be printed")
#print("this is an error:")