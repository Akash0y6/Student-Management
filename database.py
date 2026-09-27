import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anchal@01",
        database="STUDENT_MANAGEMENT"
    )
    return conn

