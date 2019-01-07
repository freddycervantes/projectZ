"""
I make sure your data goes to stockdata.db
UPDATE I AM READY
"""


class Write:

    def __init__(self):
        """
        creates a database and table if they do not exist
        """
        self.__F = self.__import_format()
        self.__db = self.__import_sqlite()
        dbconn = self.__db.connect('stockdata.db')  # Opens up database, creates one if it does not exist
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

    def __import_format(self):
        import format
        return format.Format()

    def __import_sqlite(self):
        import sqlite3
        return sqlite3

    def day_in_database(self, day, name):
        """
        This method ensures no redundant requests are called to the iex server
        :param day: datetime.datetime(year, month, day)
        :param name: ticker
        :return: True if day is in table, False else
        >>> import occasion
        >>> ticker = "SPY"
        >>> date = occasion.Occasion().get_date(2019,1,3)
        >>> m = Write()
        >>> m.day_in_database(date, ticker)
        True
        >>> m.day_in_database(occasion.Occasion().get_date(1999, 1, 1), ticker)
        False
        """
        sqlkey = self.__F.write_date(day)
        return self.key_in_table(name, sqlkey)

    def store3(self, ticker, date, data):
        """
        A storage method for long term use
        :param date: datetime.datetime(year, month, day)
        :param data: list of values for each recorded minute
        :return: True if a successful put, False else

        >>> ticker = "SPY"
        >>> from occasion import Occasion
        >>> date = Occasion().get_date(2019,1,3)
        >>> from iexfinance.stocks import get_historical_intraday
        >>> x = [i['average'] for i in get_historical_intraday(ticker, date)]
        >>> m = Write()
        >>> m.store3(ticker, date, x)
        False
        >>> ticker = "XRX"
        >>> x = [i['average'] for i in get_historical_intraday(ticker, date)]
        >>> m.store3(ticker, date, x)
        True
        >>> m.store3(ticker, date, [])
        False
        >>> m.remove_table(ticker)
        >>> m.store3(ticker, date, [1])
        True
        >>> m.remove_table(ticker)
        """
        if len(data) == 0:
            return False
        Write().pad_data(data)                                  # ensures if the data exists it is of proper length
        if self.in_whitelist(ticker):                           # no script kiddes ya lil shits
            date = self.__F.write_date(date)                    # formatting so db requests can be a specific range
            return self.put_in_stockdata(ticker, date, data)    # ensures data was properly placed
        return False

    @staticmethod
    def pad_data(data):
        """
        Since there are half trading days, this pads it with -1's
        >>> data = [i for i in range(100)]
        >>> len(data)
        100
        >>> Write.pad_data(data)
        >>> len(data)
        390
        >>> data
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        """
        while len(data) < 390:
            data += [-1]

    @staticmethod
    def in_whitelist(name):
        """
        Anti-sql injection
        :param name: List of approved Stocks
        :return: True if okay, False if not
        >>> Write.in_whitelist("GE")
        True
        >>> Write.in_whitelist("SPX")
        False
        """
        import whitelist
        return whitelist.GetItems().whitelisted(name)

    def key_in_table(self, name, sqlkey):
        """
        :param name: Ticker
        :param sqlkey: date
        :return: True if key exists, else false
        >>> t = Write()
        >>> t.key_in_table("SPX", 19991231)
        False
        >>> t.put_in_stockdata("SPX", 19991231, [i for i in range(390)])
        True
        >>> t.key_in_table("SPX", 19991231)
        True
        >>> t.key_in_table("SPX", 19991232)
        False
        >>> t.remove_table("SPX")
        """
        if not self.table_exists(name):                 # does the table exist at all?
            return False
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        c.execute("""
                    SELECT COUNT(*)
                    FROM {}
                    WHERE date = '{}'
                    """.format(name, sqlkey))
        if c.fetchone()[0] == 1:                        # Okay it does, lets see if the date has already been uploaded
            c.close()
            dbconn.close()
            return True
        c.close()
        dbconn.close()
        return False

    def put_in_stockdata(self, name, sqlkey, data):
        """
        properly formatted and ready to insert into stockdata.db
        :param name: Ticker
        :param sqlkey: date formatted
        :param data: list of 390 reals
        :return: True if inserted, False if already exists

        >>> t = Write()
        >>> t.table_exists("SPX")
        False
        >>> t.put_in_stockdata("SPX", 19991231,[i for i in range(390)])
        True
        >>> t.table_exists("SPX")
        True
        >>> t.put_in_stockdata("SPX", 19991231,[i for i in range(390)])
        False
        >>> t.put_in_stockdata("SPX", 19991232,[i for i in range(390)])
        True
        >>> t.remove_table("SPX")
        """
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        if not self.table_exists(name):                   # if not in database, create it
            self.create_table(name)
        elif self.key_in_table(name, sqlkey):             # is the key in the table!? alright nm we got it
            c.close()
            dbconn.close()
            return False
        c.execute(self.__F.write_intraday_data(name, sqlkey, data))
        c.close()
        dbconn.commit()
        dbconn.close()
        return True

    def table_exists(self, tablename):
        """
        Ensures the table exist from the onRecord table.
        :return: boolean function
        >>> import sqlite3
        >>> dbconn = sqlite3.connect('stockdata.db')
        >>> c = dbconn.cursor()
        >>> x = c.execute("INSERT INTO onRecord VALUES ('TEST')")
        >>> dbconn.commit()
        >>> t = Write()
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

    def create_table(self, name):
        """
        Creates a table with name as name
        :param name: Stock Ticker
        :return: True if successful, False else

        >>> t = Write()
        >>> t.create_table("SPX")
        True
        >>> t.create_table("SPX")
        False
        >>> t.remove_table("SPX")
        """
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        if self.table_exists(name):               #avoids redundancy
            return False
        c.execute("""
                    INSERT INTO onRecord 
                    VALUES ('{}')""".format(name))
        new_table = self.__F.write_intraday_table(name)
        c.execute(new_table)
        c.close()
        dbconn.commit()
        dbconn.close()
        return True

    def remove_table(self, name):
        """
        tableflip.jpg
        :param name: ticker
        >>> t = Write()
        >>> t.create_table("SPX")
        True
        >>> t.table_exists("SPX")
        True
        >>> t.remove_table("SPX")
        >>> t.table_exists("SPX")
        False
        """
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        c.execute("DELETE FROM onRecord WHERE stock = '{}'".format(name))   # Wether it exists or not does not matter papa bless
        try:
            c.execute("DROP TABLE {}".format(name))                         # produces error if not exicutible. SAD!
            dbconn.commit()
        except:
            dbconn.commit()
        c.close()
        dbconn.close()


if __name__=="__main__":
    import doctest
    doctest.testmod()
