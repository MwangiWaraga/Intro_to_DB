import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "username",
    password = "password"
        )

    print("Database connection open sucessfully")

except Error as e:
    print(e)


mycursor = mydb.cursor()

mycursor.execute(
    "CREATE DATABASE IF NOT EXISTS alx_book_store"
)

print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()

print("Database connection closed")