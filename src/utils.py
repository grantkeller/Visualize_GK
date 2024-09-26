import mysql.connector
from flask import jsonify

def connect_to_mysql():

    db_config = {
    'host': 'localhost',
    'database': 'projects',
    'user': 'root',
    'password': 'password'
    }

    try:
        cnx = mysql.connector.connect(db_config)
        print("Connected to MySQL database")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def query_county(con, county):
    mycursor = con.cursor()
    query = f"SELECT * FROM state_county WHERE County={county}"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return jsonify(result)