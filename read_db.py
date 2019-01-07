"""

"""


class Read:

    def __init__(self):
        self.__F = self.__import_format()
        self.__db = self.__import_sqlite()

    def __import_format(self):
        import format
        return format.Format()

    def __import_sqlite(self):
        import sqlite3
        return sqlite3

    def read_all(self, name):
        """
        :param name: Ticker
        :return: All clensed data from a specific ticker.
        >>> R = Read()
        >>> R.read_all("FDHKJH")
        False
        >>> R.read_all("SPY")[0]
        271.593
        """
        if not self.table_exists(name):
            return False
        conn = self.__db.connect("stockdata.db")
        c = conn.cursor()
        c.execute(self.__F.read_intraday_table_all(name))
        raw = [list(i) for i in c.fetchall()]
        clensed = []
        for i in raw:
            clensed += i[1:]
        clensed = [i for i in clensed if i != -1]
        return clensed

    def table_exists(self, tablename):
        """
        Ensures the table exist from the onRecord table.
        :return: boolean function
        >>> import sqlite3
        >>> dbconn = sqlite3.connect('stockdata.db')
        >>> c = dbconn.cursor()
        >>> x = c.execute("INSERT INTO onRecord VALUES ('TEST')")
        >>> dbconn.commit()
        >>> t = Read()
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
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        c.execute("""
                SELECT COUNT(*)
                FROM onRecord
                WHERE stock = '{0}'
                """.format(tablename))
        if c.fetchone()[0] == 1:                    # I dunno, I think in 5 years I could figure out what this does
            c.close()
            return True
        c.close()
        dbconn.close()
        return False

if __name__=="__main__":
    import doctest
    doctest.testmod()
