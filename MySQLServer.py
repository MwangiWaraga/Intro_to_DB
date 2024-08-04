import mysql.connector

try:
    # Establish a connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Waraga@designs6"
    )

    if mydb.is_connected():
        print("Database connection opened successfully")

    mycursor = mydb.cursor()

    # Create the database if it does not exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

    # Close cursor and connection inside the try block
    mycursor.close()
    mydb.close()
    print("Database connection closed")

except Error as e:
    # This block catches and handles any connection errors
    print(f"Error: {e}")