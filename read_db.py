"""

"""


class Read:

    def __init__(self):
        self.__format = self.__import_format()
        self.__db = self.__import_sqlite()

    def __import_format(self):
        import format
        return format.Format()

    def __import_sqlite(self):
        import sqlite3
        return sqlite3

    def read_all_five(self, name):
        t = name + "5"
        if not self.table_exists(t):
            return False
        conn = self.__db.connect("stockdata.db")
        c = conn.cursor()
        c.execute(self.__format.read_five_all(t))
        raw = c.fetchall()
        c.close()
        conn.close()
        return raw


    def read_all_intra(self, name):
        """
        :param name: Ticker
        :return: All clensed data from a specific ticker.
        >>> R = Read()
        >>> R.read_all_intra("FDHKJH")
        False
        >>> R.read_all_intra("SPY")[0]
        271.593
        """
        if not self.table_exists(name):
            return False
        conn = self.__db.connect("stockdata.db")
        c = conn.cursor()
        c.execute(self.__format.read_intraday_table_all(name))
        raw = [list(i) for i in c.fetchall()]
        c.close()
        conn.close()
        clensed = []
        for i in raw:
            clensed += i[1:]
        clensed = [i for i in clensed if i != -1]
        # Append the rest of today
        return clensed + self.append_today(name)

    def append_today(self, name):
        """
        :param name: ticker
        :return: list of today
        >>> R = Read()
        >>> R.append_today("SPY")
        []
        >>> len(R.append_today("XRX")) > 0
        True
        """
        import write_dat
        import occasion
        import fetch_data
        W = write_dat.Write()
        sqlkey = self.__format.write_date(occasion.Occasion().today())
        if W.key_in_table(name, sqlkey):
            return []
        F = fetch_data.Fetch()
        return [i for i in F.intraday_average_price(name, occasion.Occasion().today()) if i != -1]



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
