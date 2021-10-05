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
    except Error as e:
        print(e)

    return conn


def create_favmovies(conn, favmovies):
    """
    Create a new favmovies into the favmovies table
    :param conn:
    :param favmovies:
    :return: project id
    """
    sql = ''' INSERT INTO favmovies(movie_name, lead_actor, actress, year_of_release, dir_name)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, favmovies)
    conn.commit()
    return cur.lastrowid



def main():
    database = r"C:\sqlite\db\movie.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new favmovies
        favmovies_1 = ('Appu', 'Puneeth Rajkumar', 'Rakshitha', '2001', 'Sundar');
        favmovies_2 = ('Airavatha', 'Darshan', 'Urvashi', '2017', 'Ramesh');
        favmovies_3 = ('Hebbuli', 'Sudeep', 'Amla Pual', '2018', 'Srinivas');
        favmovies_4 = ('Tagaru', 'Shiv Rajkumar', 'Bhavana', '2018', 'Ravi');
        favmovies_5 = ('Avne Srimannaryana', 'Rakshith Shetty', 'Sanvi', '2019', 'Rakshith');
        create_favmovies(conn, favmovies_1)
        create_favmovies(conn, favmovies_2)
        create_favmovies(conn, favmovies_3)
        create_favmovies(conn, favmovies_4)
        create_favmovies(conn, favmovies_5)
        

if __name__ == '__main__':
    main()
