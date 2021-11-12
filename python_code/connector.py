import mysql.connector
from mysql.connector import Error


try:
    hospital_database = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        passwd="",
        database="hospital")
    if hospital_database.is_connected():
        print("Connection with Database Successfull")
        cursor = hospital_database.cursor()
        query = 'select * from patients'
        cursor.execute(query)
        table_rows = cursor.fetchall()

except Error as e:
    print("Error while connectng to MySQL", e)
