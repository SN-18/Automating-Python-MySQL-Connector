import mysql.connector
import sys
import os
os.system('sudo /etc/init.d/mysql start')


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

