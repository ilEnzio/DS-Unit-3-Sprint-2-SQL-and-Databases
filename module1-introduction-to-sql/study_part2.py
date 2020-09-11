import sqlite3
import pprint


def connect_to_chinook(db_name="Chinook_Sqlite.sqlite"):
    return sqlite3.connect(db_name)


def execute_query(connection, cursor, query):
    with connection:
        cursor.execute(query)

        return cursor.fetchall()


# Find the average invoice total for each customer, return the details for the first 5 ID's

def get_average_invoice_five_total():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    AVG_INVOICE_TOTAL = """
        SELECT AVG(Total) as avg_invoice, *
        FROM Invoice
        GROUP BY CustomerId
        LIMIT 5
        """

    results = execute_query(connection, cursor, AVG_INVOICE_TOTAL)

    pp = pprint.PrettyPrinter(width=150, compact=True)

    # print(f"The list of students are... {results}.")
    print("5 Average Customer Invoices:")

    pp.pprint(results)

# Return all columns in Customer for the first 5 customers residing in the United States


def get_five_customers_in_usa():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    FIVE_CUSTOMERS_IN_USA = """
        SELECT *
        FROM Customer
        WHERE Country = "USA"
        LIMIT 5
        """

    results = execute_query(connection, cursor, FIVE_CUSTOMERS_IN_USA)

    pp = pprint.PrettyPrinter(width=150, compact=True)

    # print(f"The list of students are... {results}.")
    print("5 Customers in USA:")

    pp.pprint(results)

# Which employee does not report to anyone?


def get_empl_no_boss():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    NO_BOSS = """
        SELECT FirstName,LastName
        FROM Employee
        WHERE ReportsTo IS NULL
        """

    results = execute_query(connection, cursor, NO_BOSS)

    print(f"The only one with no boss is {results[0][0]} {results[0][1]}.")


# Find the number of unique composers

def get_num_unique_composers():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    NUM_UNIQUE_COMPOSERS = """
        SELECT COUNT(DISTINCT Composer)
        FROM Track  
        """

    results = execute_query(connection, cursor, NUM_UNIQUE_COMPOSERS)

    print(f"The number of unique composers is {results[0][0]}.")


# How many rows are in the Track table?​

def get_rows_in_track():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    NUM_ROWS_IN_TRACK = """
        SELECT COUNT(*)
        FROM Track 
        """

    results = execute_query(connection, cursor, NUM_ROWS_IN_TRACK)

    print(f"The number of rows in the Track table is {results[0][0]}.")


# Get the name of all Black Sabbath tracks and the albums they came off of

def get_all_bs_tracks_albums():

    connection = connect_to_chinook()
    cursor = connection.cursor()

    BLACKSAB_TRACKS = """
        SELECT 
        comp_artist."Name" as a_name, Title, Track."Name" as t_name
        FROM Track
        JOIN
            (SELECT *
            FROM Album
            JOIN Artist ON Artist.ArtistId = Album.ArtistId
            WHERE Artist."Name" = "Black Sabbath") comp_artist
        ON Track."Name" = comp_artist."Name"
        """

    results = execute_query(connection, cursor, BLACKSAB_TRACKS)

    pp = pprint.PrettyPrinter(width=80, compact=True)

    # print(f"The list of students are... {results}.")
    print("BLACK SABBATH TRACKS:")

    pp.pprint(results)


# What is the most popular genre by number of tracks?


# Find all customers that have spent over $45
# Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.

if __name__ == "__main__":

    # display results
    # print(results)

    # connect to database
    connection = connect_to_chinook()

    # make a cursor (something that iterates over DB)
    cursor = connection.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    # execute_query(connection, cursor, INSERT_THUNDERCATS)
    get_average_invoice_five_total()
    get_five_customers_in_usa()
    get_empl_no_boss()
    get_num_unique_composers()
    get_rows_in_track()
    get_all_bs_tracks_albums()

    cursor.close()

    # print(results2)
