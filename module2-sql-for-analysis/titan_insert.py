import psycopg2

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values


import pandas as pd

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)


# A "cursor", a structure to iterate over db records to perform queries

cursor = connection.cursor()
print("CURSOR:", cursor)

# prepare the data

titan_df = pd.read_csv(
    "https://raw.githubusercontent.com/ilEnzio/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv")

# this basically takes all the data and pairs the columns
# with the values as tuples
# but this might be wrong format for tuple list
data_tuple_list = []
# for x in range(0, len(titan_df.columns)):
#     temp_tup = (titan_df.columns[x], list(titan_df.iloc[:, x].values))
#     data_tuple_list.append(temp_tup)

#   tuple list vers 2!

# records = titan_df.to_records(index=False)
# data_tuple_list = list(records)

# tuple list vers 3

data_tuple_list = [list(row) for row in titan_df.itertuples(index=False)]

# Now I need to learn the query

# Create the table with cursor
CREATE_TABLE = """ 
    DROP TABLE IF EXISTS titanic_passengers;
                    CREATE TABLE titanic_passengers (
        Survived int,
        Pclass int,
        Name varchar(100),
        Sex varchar(100),
        Age float,
        Siblings_Spouses_Aboard int,
        Parents_Children_Aboard int,
        Fare float
    );"""


cursor.execute(CREATE_TABLE)


insertion_query = "INSERT INTO titanic_passengers (Survived, Pclass, Name,  Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) VALUES %s"

execute_values(cursor, insertion_query, data_tuple_list)

connection.commit()

cursor.close()
connection.close()
