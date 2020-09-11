import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# db_name = "rpg_db.sqlite3"


def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):

    cursor.execute(query)

    return cursor.fetchall()


# SHOW COLUMNS = "SHOW COLUMNS FROM {db_name}"

# How many total Characters are there?
TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character
    """


# How many of each specific subclass?

TOTAL_CLERICS = """
    SELECT count(*)
    FROM charactercreator_cleric
    """

TOTAL_FIGHTERS = """
    SELECT count(*)
    FROM charactercreator_fighter
    """

TOTAL_MAGE = """
    SELECT count(*)
    FROM charactercreator_mage
    """

TOTAL_NECROMANCER = """
    SELECT count(*)
    FROM charactercreator_necromancer
    """
TOTAL_THIEF = """
    SELECT count(*)
    FROM charactercreator_thief
    """

# How many total Items?

TOTAL_ITEM = """
    SELECT count(*) as row_count
    FROM armory_item
    """


# How many of the Items are weapons?
WEAPONS_COUNT = """
    SELECT 
	    count(*) as weapons
    FROM armory_item
    JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id
"""

#  How many are not?

NON_WEAPONS = """
   
"""


# How many Items does each character have?
# (Return first 20 rows)

# How many Weapons does each character have?
# (Return first 20 rows)

# On average, how many Items does each Character have?


# On average, how many Weapons does each character have?
#  row per character = 302
# columns, character

AVERAGE_WEAPON_PER_CHAR = """
    SELECT AVG(weapon_count) as avg_weapons_per_char
    FROM (

        SELECT 
            c.character_id,
            -- c.name,
            -- inv.*,
            -- wep.*,
            count(distinct wep.item_ptr_id) as weapon_count
        FROM charactercreator_character c
        LEFT JOIN charactercreator_character_inventory inv  ON c.character_id = inv.character_id
        LEFT JOIN armory_weapon wep ON inv.item_id = wep.item_ptr_id
        GROUP BY c.character_id
        ) subq
    """

# How many rows in buddy movies db

# B_MOVIE_ROW_COUNT = """
#     SHOW TABLES
#     """
# this makes like a semi-API type object? which we use to use
# sqlaclchemy functions


engine = create_engine('sqlite://', echo=False)

b_movie_db = pd.read_csv(
    "/Users/kellycho/Desktop/Repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv")

# take the space out of the column name just in case there is a problem
# with sql syntax later.
b_movie_db["User_Id"] = b_movie_db["User Id"]
b_movie_db.drop("User Id", axis=1)

# Create a table
CREATE_MOVIE_TABLE = """
CREATE TABLE buddymov(
    User_Id VARCHAR(100),
	Sports INT,
	Religous INT,
	Nature int,
	Theatre int,
	Shopping int,
	Picnic int
);
"""


def connect_to_buddy_db(db_name="buddbymove_holidayiq.sqlite3"):
    return sqlite3.connect(db_name)


def write_df_to_db(df, sql_str, connect):
    # this injects the df
    # df.to_sql(name=sql_str, con=engine, if_exists="append")
    df.to_sql(name=sql_str, conn, if_exists="replace")


if __name__ == "__main__":

    # connect to database
    conn = connect_to_db()

    # make a cursor (something that iterates over DB)
    curs = conn.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    results = execute_query(curs, TOTAL_CHARACTERS)
    curs.close()
    # display results
    # print(results)

    conn2 = connect_to_buddy_db()
    curs2 = conn2.cursor()

    execute_query(curs2, CREATE_MOVIE_TABLE)

    write_df_to_db(b_movie_db, "buddymov", conn2)

    # results2 = execute_query(curs2, B_MOVIE_ROW_COUNT)
    curs2.close()
    # print(results2)
