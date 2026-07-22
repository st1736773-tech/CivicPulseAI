import sqlite3


DATABASE = "civicpulse.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )

    """)


    conn.commit()

    conn.close()



def add_user(username,email,password):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO users(username,email,password)
        VALUES(?,?,?)
        """,
        (username,email,password)
    )


    conn.commit()

    conn.close()



def get_user(email):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=?
        """,
        (email,)
    )


    user = cursor.fetchone()


    conn.close()


    return user