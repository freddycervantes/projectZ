"""
I make sure your data goes to stockdata.db
UPDATE I AM READY
"""


def table_exists(tablename):
    return None

class Write:

    def __init__(self):
        """
        creates a database and table if they do not exist
        """
        import sqlite3
        dbconn = sqlite3.connect('stockdata.db')  # Opens up database, creates one if it does not exist
        c = dbconn.cursor()
        try:
            # checks to see if onRecord exists, creates the table if it does not
            c.execute(
                "CREATE TABLE onRecord (stock text PRIMARY KEY)")
        except:
            c.close()
        c.close()
        dbconn.commit()
        dbconn.close()

    def table_exists(self, tablename):
        """
        Ensures the table exist from the onRecord table.
        :return: boolean function
        >>> t = Write()
        >>> import sqlite3
        >>> dbconn = sqlite3.connect('stockdata.db')
        >>> c = dbconn.cursor()
        >>> x = c.execute("INSERT INTO onRecord VALUES ('TEST')")
        >>> dbconn.commit()
        >>> t.table_exists("TEST")
        True
        >>> t.table_exists("test1")
        False
        >>> x = c.execute("DELETE FROM onRecord WHERE stock = 'TEST'")
        >>> dbconn.commit()
        >>> t.table_exists("TEST")
        False
        >>> c.close()
        >>> dbconn.close()
        """
        import sqlite3
        dbconn = sqlite3.connect('stockdata.db')
        dbcur = dbconn.cursor()
        dbcur.execute("""
                SELECT COUNT(*)
                FROM onRecord
                WHERE stock = '{0}'
                """.format(tablename))
        if dbcur.fetchone()[0] == 1:                    # I dunno, I think in 5 years I could figure out what this does
            dbcur.close()
            return True
        dbcur.close()
        dbconn.close()
        return False



if __name__=="__main__":
    import doctest
    doctest.testmod()