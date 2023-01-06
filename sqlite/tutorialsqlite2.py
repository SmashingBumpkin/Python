import sqlite3

class databaseTool:
    def connect(name = "tutorial.db"):
        self.con = sqlite3.connect(name)
        """
        The returned Connection object con represents the connection to the on-disk database.

        In order to execute SQL statements and fetch results from SQL queries, we will 
        need to use a database cursor. Call con.cursor() to create the Cursor:
        """
        self.cur = con.cursor()
        
    def create_new():
        """
        Now that we’ve got a database connection and a cursor, we can create a database 
        table movie with columns for title, release year, and review score. For 
        simplicity, we can just use column names in the table declaration – thanks to 
        the flexible typing feature of SQLite, specifying the data types is optional. 
        Execute the CREATE TABLE statement by calling cur.execute(...):
        """
        self.cur.execute("CREATE TABLE movie(title, year, score)")
        
    









"""
We can verify that the new table has been created by querying the sqlite_master 
table built-in to SQLite, which should now contain an entry for the movie table 
definition (see The Schema Table for details). Execute that query by calling 
cur.execute(...), assign the result to res, and call res.fetchone() to fetch 
the resulting row:
"""
    def fetch_one(name = "name")
        res = cur.execute("SELECT {name} FROM sqlite_master")

        res.fetchone()
        """

        We can see that the table has been created, as the query returns a tuple 
        containing the table’s name. If we query sqlite_master for a non-existent 
        table spam, res.fetchone() will return None:

        """
        
    def fetch_spam():
    """If we query sqlite_master for a non-existent 
    table spam, res.fetchone() will return None:"""
        res = self.cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

        res.fetchone() is None

"""
Now, add two rows of data supplied as SQL literals by executing an INSERT statement, once again by calling cur.execute(...):
"""
    def insert_movies():
        
        self.cur.execute("""
            INSERT INTO movie VALUES
                ('Monty Python and the Holy Grail', 1975, 8.2),
                ('And Now for Something Completely Different', 1971, 7.5)
        """)
        """
        The INSERT statement implicitly opens a transaction, which needs to be
        committed before changes are saved in the database (see Transaction control 
        for details). Call con.commit() on the connection object to commit the transaction:
        """
        self.con.commit()
        """
        We can verify that the data was inserted correctly by executing a SELECT
        query. Use the now-familiar cur.execute(...) to assign the result to 
        res, and call res.fetchall() to return all resulting rows:
        """
        
        res = self.cur.execute("SELECT score FROM movie")
        
        res.fetchall()

        """
        The result is a list of two tuples, one per row, each containing that row’s score value.
        
        Now, insert three more rows by calling cur.executemany(...):
        """
        data = [
            ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
            ("Monty Python's The Meaning of Life", 1983, 7.5),
            ("Monty Python's Life of Brian", 1979, 8.0),
        ]
        self.cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
        self.con.commit()  # Remember to commit the transaction after executing INSERT.

        """
        Notice that ? placeholders are used to bind data to the query. Always use 
        placeholders instead of string formatting to bind Python values to SQL 
        statements, to avoid SQL injection attacks (see How to use placeholders to 
        bind values in SQL queries for more details).
        
        We can verify that the new rows were inserted by executing a SELECT query, this 
        time iterating over the results of the query:
        """
        
        for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
        
            print(row)
        """
        
        Each row is a two-item tuple of (year, title), matching the columns selected in the query.
        
        Finally, verify that the database has been written to disk by calling con.close() to close the existing connection, opening a new one, creating a new cursor, then querying the database:
        """
        
        con.close()
    def reconnect():

         