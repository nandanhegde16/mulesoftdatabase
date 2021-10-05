import sqlite3
from sqlite3 import Error


def create_connection(movie):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(movie)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\movie.db"

    sql_create_favmovies_table = """ CREATE TABLE IF NOT EXISTS favmovies (
                                        movie_name varchar(30),
                                        lead_actor varchar(25),
                                        actress varchar(25),
                                        year_of_release varchar(5),
                                        dir_name varchar(25)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create favmovies table
        create_table(conn, sql_create_favmovies_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
