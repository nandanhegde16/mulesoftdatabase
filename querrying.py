import sqlite3
from sqlite3 import Error


def create_connection(movie):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(movie)
    except Error as e:
        print(e)

    return conn


def select_all_favmovies(conn):
    """
    Query all rows in the favmovies table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM favmovies")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_favmovies_by_lead_actor(conn, lead_actor):
    """
    Query favmovies by lead_actor
    :param conn: the Connection object
    :param lead_actor:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT movie_name FROM favmovies WHERE lead_actor=?", (lead_actor,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\sqlite\db\movie.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all favmovies")
        select_all_favmovies(conn)
        
        print("2. Query favmovies by lead_actor:")
        select_favmovies_by_lead_actor(conn, 'Darshan')


if __name__ == '__main__':
    main()
