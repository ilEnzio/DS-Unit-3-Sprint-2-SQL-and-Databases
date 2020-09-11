import sqlite3
import pprint


# connect to db northwind_sqlite3


def connect_to_nw_db(db_name="northwind_small.sqlite3"):
    return sqlite3.connect(db_name)


# execute queries. use context syntax to ensure commit/close

def execute_query(connection, cursor, query):
    with connection:
        cursor.execute(query)

        return cursor.fetchall()


def display_columns():

    connection = connect_to_nw_db()
    cursor = connection.cursor()

    DISPLAY_COLUMNS = """
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' ORDER BY name;
        """

    results = execute_query(connection, cursor, DISPLAY_COLUMNS)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    print(f"All columns...:")

    pp.pprint(results)

# What are the ten most expensive items (per unit price) in the database?


def get_top_ten_expensive():

    connection = connect_to_nw_db()
    cursor = connection.cursor()

    TOP_TEN_EXPENSIVE = """
        SELECT ProductName, UnitPrice
        FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10
        """

    results = execute_query(connection, cursor, TOP_TEN_EXPENSIVE)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    print(f"The TOP 10 most expensive products are:")

    pp.pprint(results)

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)


def get_empl_ave_age_at_hire():

    connection = connect_to_nw_db()
    cursor = connection.cursor()

    AVG_AGE_AT_HIRE = """
        SELECT AVG(age)
        FROM
	        (SELECT 
			FirstName,
			LastName
			HireDate, 
			BirthDate,
			(HireDate - BirthDate) as age
	        FROM Employee)
        """

    results = execute_query(connection, cursor, AVG_AGE_AT_HIRE)

    print(f"The average age of an employee at hire date is {results[0][0]}.")

# (Stretch) How does the average age of employee at hire vary by city?


# What are the ten most expensive items (per unit price) in the database and their suppliers?

def get_top_ten_price_supplier():

    connection = connect_to_nw_db()
    cursor = connection.cursor()

    TOP_TEN_W_SUPPLIER = """
        SELECT 
            ProductName, 
            CompanyName, 
            UnitPrice
        FROM Product
        JOIN Supplier On Product.SupplierId = Supplier.Id
        ORDER BY UnitPrice DESC
        LIMIT 10
        """

    results = execute_query(connection, cursor, TOP_TEN_W_SUPPLIER)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    print(f"The TOP 10 most expensive products AND suppliers are:")

    pp.pprint(results)
# What is the largest category (by number of unique products in it)?


def get_largest_category():

    connection = connect_to_nw_db()
    cursor = connection.cursor()

    LARGEST_CAT = """
        SELECT
            CategoryId,
            COUNT(CategoryId) as countOf
        FROM
            (SELECT *
            FROM Product
            JOIN Supplier
                ON Product.SupplierId = Supplier.Id)
        GROUP By CategoryId
        ORDER By countOf DESC
        LIMIT 1
        """

    results = execute_query(connection, cursor, LARGEST_CAT)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    # print(f"The largest category of product is:")
    print(
        f"The largest category of product is: {results[0][0]}. With a count of: {results[0][1]}.")
    # pp.pprint(results)

# (Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.


if __name__ == "__main__":

    # connect to database
    connection = connect_to_nw_db()

    # make a cursor (something that iterates over DB)
    cursor = connection.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    # results = execute_query(connection, cursor, CREATE_DEMO_TABLE)

    get_top_ten_expensive()
    get_empl_ave_age_at_hire()
    get_top_ten_price_supplier()
    get_largest_category()

    cursor.close()
    # print(results2)
