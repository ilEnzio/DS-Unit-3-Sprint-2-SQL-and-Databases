import psycopg2

import os
from dotenv import load_dotenv
import psycopg2

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
data_tuple_list = []
for x in range(0, len(titan_df.columns)):
    temp_tup = (titan_df.columns[x], list(titan_df.iloc[:, x].values))
    data_tuple_list.append(temp_tup)

# Now I need to learn the query
