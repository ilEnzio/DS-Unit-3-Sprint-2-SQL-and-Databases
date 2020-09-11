import sqlite3
import pandas as pd
from sqlalchemy import create_engine


def connect_to_buddy_db(db_name="buddbymove_holidayiq.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(connection, cursor, query):
    with connection:
        cursor.execute(query)

        return cursor.fetchall()


def write_df_to_db(df, sql_str, connect):
    # this injects the df
    # df.to_sql(name=sql_str, con=engine, if_exists="append")
    with connect:
        df.to_sql(name=sql_str, con=connect, if_exists="replace")


# Create a table
CREATE_MOVIE_TABLE = """
CREATE TABLE buddymov(
    User_Id VARCHAR(100),
	Sports INT,
	Religous INT,
	Nature INT,
	Theatre INT,
	Shopping INT,
	Picnic INT
);
"""
b_movie_db = pd.read_csv(
    "/Users/kellycho/Desktop/Repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv")

b_movie_db["User_Id"] = b_movie_db["User Id"]
b_movie_db.drop("User Id", axis=1)


if __name__ == "__main__":

    # display results
    # print(results)

    # connect to database
    conn2 = connect_to_buddy_db()

    # make a cursor (something that iterates over DB)
    curs2 = conn2.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    results2 = execute_query(conn2, curs2, CREATE_MOVIE_TABLE)
    # conn2.commit()
    write_df_to_db(b_movie_db, "buddymov", conn2)

    # results2 = execute_query(curs2, B_MOVIE_ROW_COUNT)

    curs2.close()
    # print(results2)
