import sqlite3
import pprint

# Create a new db called study_part1.sqlite3


def connect_to_stpart1(db_name="study_part1.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(connection, cursor, query):
    with connection:
        cursor.execute(query)

        return cursor.fetchall()


CREATE_STUDENTS_TABLE = """
CREATE TABLE students(
	student VARCHAR(100),
    studied VARCHAR(100),
    grade INT,
    age INT,
    sex VARCHAR(50));
    """

# insert the  data
INSERT_THUNDERCATS = """
INSERT INTO students (student, studied, grade, age, sex)
VALUES('Lion-O', 'True', 85, 24, 'Male'),
 ('Cheetara', 'True', 95, 22, 'Female'),
 ('Mumm-Ra', 'False', 65, 153, 'Male'),
 ('Snarf', 'False', 70, 15, 'Male'),
 ('Panthro', 'True', 80, 30, 'Male');
 """

# What is the average age? Expected Result 48.8


def get_avg_age():

    connection = connect_to_stpart1()
    cursor = connection.cursor()

    AVG_AGE = """
        SELECT AVG(age)
        FROM students
        """

    results = execute_query(connection, cursor, AVG_AGE)

    print(f"The average age of the students is {results[0][0]}.")

#  What are the name of the female students? Expected Result - 'Cheetara'


def get_fem_student_name():

    connection = connect_to_stpart1()
    cursor = connection.cursor()

    FEM_NAME = """
        SELECT student
        FROM students
        WHERE sex = "Female"
        """

    results = execute_query(connection, cursor, FEM_NAME)

    print(f"The Female students are {results[0][0]}.")


# How many students studied? Expected Results - 3
def get_student_who_studied():

    connection = connect_to_stpart1()
    cursor = connection.cursor()

    WHO_STUDIED = """
        SELECT COUNT (*)
        FROM students
        WHERE studied = "True"
        """

    results = execute_query(connection, cursor, WHO_STUDIED)
    print(f"The number of students who studied is {results[0][0]}.")


# Return all students and all columns, sorted by student names in alphabetical order.

def get_all_students_ordered():

    connection = connect_to_stpart1()
    cursor = connection.cursor()

    ORDERED_STUDENTS = """
        SELECT *
        FROM students
        ORDER BY student
        """

    results = execute_query(connection, cursor, ORDERED_STUDENTS)

    pp = pprint.PrettyPrinter(indent=4)

    # print(f"The list of students are... {results}.")
    print(f"The list of students are:")

    pp.pprint(results)


if __name__ == "__main__":

    # display results
    # print(results)

    # connect to database
    connection = connect_to_stpart1()

    # make a cursor (something that iterates over DB)
    cursor = connection.cursor()

    # Write query (inside python this will be a string)
    # Execute query
    # Fetch results
    # execute_query(connection, cursor, INSERT_THUNDERCATS)
    get_avg_age()
    get_fem_student_name()
    get_student_who_studied()
    get_all_students_ordered()

    cursor.close()

    # print(results2)
