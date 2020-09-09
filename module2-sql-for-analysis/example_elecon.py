import psycopg2

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)
# exit()

# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)


# A "cursor", a structure to iterate over db records to perform queries


cursor = connection.cursor()
print("CURSOR:", cursor)


# An example query

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)
# Note - nothing happened yet! We need to actually *fetch* from the cursor

result = cursor.fetchall()

print(result)


# Insert Data

insertion_sql = """
INSERT INTO test_table (name, data)
		VALUES('A row name', null), 
		('Another row, with JSON', '{ "a": 1, "b": ["dog", "cat", 42], "c" : true }'::JSONB);
        """

cursor.execute(insertion_sql)

# Acually Save the TRansactions

connection.commit()

cursor.close()
connection.close()
