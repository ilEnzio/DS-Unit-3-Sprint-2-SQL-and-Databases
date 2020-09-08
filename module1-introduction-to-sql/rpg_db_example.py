import sqlite3


def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):

    # this is takig the given cursor, and executing the given query
    # this is the total results of the query in another table.
    cursor.execute(query)

    # this is fetching and return the results.
    return cursor.fetchall()


# this is a stament,but not results
GET_CHARACTERS = "SELECT * FROM charactercreator_character;"

GET_CHARACTERS2 = """
    SELECT * 
    FROM charactercreator_character;
    """


if __name__ == "__main__":

    # connect to database
    conn = connect_to_db()

    # make a cursor (something that iterates over DB)
    curs = conn.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    results = execute_query(curs, GET_CHARACTERS)

    # display results
    print(results)
