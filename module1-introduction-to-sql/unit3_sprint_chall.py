import sqlite3
import pprint

# connect to db demo_data.sqlite3


def connect_to_demo_db(db_name="demo_data.sqlite3"):
    return sqlite3.connect(db_name)


# execute queries. use context syntax to ensure commit/close

def execute_query(connection, cursor, query):
    with connection:
        cursor.execute(query)

        return cursor.fetchall()

# display the demo data to make sure it's there


def create_demo_table():

    connection = connect_to_demo_db()
    cursor = connection.cursor()

    DROP_IF = """
    DROP TABLE IF EXISTS demo_table;
    """

    CREATE_DEMO_TABLE = """
    CREATE TABLE demo_table(
        s VARCHAR(10),
	    x INT,
	    y INT
    );
    """
    execute_query(connection, cursor, DROP_IF)
    execute_query(connection, cursor, CREATE_DEMO_TABLE)

    print(f"Table Created...:")


def insert_demo_data():

    connection = connect_to_demo_db()
    cursor = connection.cursor()

    INSERT_DEMO_DATA = """
        INSERT INTO demo_table(s,x,y)
        VALUES ("g", 3, 9), 
		        ("v", 5, 7),
		        ("f", 8, 7);
        """

    results = execute_query(connection, cursor, INSERT_DEMO_DATA)


def display_data():

    connection = connect_to_demo_db()
    cursor = connection.cursor()

    DISPLAY_DATA = """
        SELECT *
        FROM demo_table
        """

    results = execute_query(connection, cursor, DISPLAY_DATA)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    print(f"All data...:")

    pp.pprint(results)


# Count how many rows you have - it should be 3!

def get_demo_row_count():
    connection = connect_to_demo_db()
    cursor = connection.cursor()

    NUM_ROWS = """
        SELECT COUNT(*)
        FROM demo_table
        """

    results = execute_query(connection, cursor, NUM_ROWS)

    print(f"The number of rows in the Demo table is {results[0][0]}.")

# How many rows are there where both x and y are at least 5?


def get_five_or_more_row_count():
    connection = connect_to_demo_db()
    cursor = connection.cursor()

    FIVE_PLUS_NUM_ROWS = """
        SELECT COUNT(*)
        FROM demo_table
        WHERE x >=5 AND y >=5
        """

    results = execute_query(connection, cursor, FIVE_PLUS_NUM_ROWS)

    print(f"The number of rows where x and y are 5+ is {results[0][0]}.")

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?


def get_unique_y_count():
    connection = connect_to_demo_db()
    cursor = connection.cursor()

    UNIQUE_Y_COUNT = """
        SELECT COUNT(DISTINCT y)
        FROM demo_table
        """

    results = execute_query(connection, cursor, UNIQUE_Y_COUNT)

    print(f"There are {results[0][0]} unique values for y.")


if __name__ == "__main__":

    # display results
    # print(results)

    # connect to database
    connection = connect_to_demo_db()

    # make a cursor (something that iterates over DB)
    cursor = connection.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    # results = execute_query(connection, cursor, CREATE_DEMO_TABLE)

    create_demo_table()  # <<<<---- only run once
    insert_demo_data()  # <<<<---- only run once
    display_data()
    get_demo_row_count()
    get_five_or_more_row_count()
    get_unique_y_count()

    cursor.close()
    # print(results2)
