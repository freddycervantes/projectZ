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
        self.__O = self.__import_occasion()
        self.__Fetch = self.__import_fetch_data()
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

    @staticmethod
    def __import_format():
        import format
        return format.Format()

    @staticmethod
    def __import_sqlite():
        import sqlite3
        return sqlite3

    @staticmethod
    def __import_occasion():
        import occasion
        return occasion.Occasion()

    @staticmethod
    def __import_fetch_data():
        import fetch_data
        return fetch_data.Fetch()

    def day_in_database(self, day, name):  #
        """
        This method ensures no redundant requests are called to the iex server
        :param day: datetime.datetime(year, month, day)
        :param name: ticker
        :return: True if day is in table, False else"""

        sqlkey = self.__F.write_date(day)
        return self.key_in_table(name, sqlkey)

    def store5(self, ticker):  # #######
        """
        >>> W = Write()
        >>> import sqlite3
        >>> dbconn = sqlite3.connect("stockdata.db")
        >>> import occasion
        >>> c = dbconn.cursor()
        >>> W.store5("XRXXX")
        False
        >>> W.store5("XRX")
        True
        >>> W.store5("XRX")
        False
        >>> x = c.execute("SELECT MAX(date) FROM XRX5")
        >>> day = c.fetchall()[0][0]
        >>> x = c.execute("DELETE FROM XRX5 WHERE date = {}".format(day))
        >>> dbconn.commit()
        >>> W.store5("XRX")
        True
        >>> x = c.execute("DELETE FROM onRecord WHERE stock = 'XRX5'")
        >>> x = c.execute("DROP TABLE XRX5")
        >>> c.close()
        >>> dbconn.commit()
        >>> dbconn.close()
        """
        import whitelist
        if ticker not in whitelist.GetItems().approved_stocks():
            return False
        t = ticker + "5"
        start, end = self.__O.five_years()
        if not self.table_exists(t):
            self.__create_five_table(t)
            self.__update5(ticker, start, end)
        else:
            start = self.__find_start(t)
            if start == end:
                return False
            start = self.__O.add_one_day(start)
            self.__update5(ticker, start, end)
        return True

    def __create_five_table(self, name):
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        c.execute("""INSERT INTO onRecord VALUES ('{}')""".format(name))
        new_table = self.__F.make_five_table(name)
        c.execute(new_table)
        c.close()
        dbconn.commit()
        dbconn.close()

    def __find_start(self, t):  # #########
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        c.execute("SELECT MAX(date) FROM {}".format(t))
        day = c.fetchall()[0][0]
        year, month, day = int(day/10000), int((day % 10000)/100), day % 100
        c.close()
        dbconn.close()
        return self.__O.get_date(year, month, day)

    def __update5(self, ticker, start, end):  # #########
        date_map = self.__Fetch.get_raw_days(ticker, start, end)
        t = ticker + "5"
        dbconn = self.__db.connect('stockdata.db')
        c = dbconn.cursor()
        for i in date_map.keys():
            new_input = self.__F.write_five_day(t, self.__F.date_text_to_int(i), date_map[i]['close'], date_map[i]['volume'])
            c.execute(new_input)
        c.close()
        dbconn.commit()
        dbconn.close()

    def store3(self, ticker, date, data):  #
        """A storage method for long term use
        :param date: datetime.datetime(year, month, day)
        :param data: list of values for each recorded minute
        :return: True if a successful put, False else"""
        if len(data) == 0:
            return False
        Write().__pad_data(data)                                # ensures if the data exists it is of proper length
        if self.in_whitelist(ticker):                           # no script kiddes ya lil shits
            date = self.__F.write_date(date)                    # formatting so db requests can be a specific range
            return self.put_in_stockdata(ticker, date, data)    # ensures data was properly placed
        return False

    @staticmethod
    def __pad_data(data):
        """Since there are half trading days, this pads it with -1's"""
        while len(data) < 390:
            data += [-1]

    @staticmethod
    def in_whitelist(name):  #
        """Anti-sql injection :return: True if okay, False if not"""
        import whitelist
        return whitelist.GetItems().whitelisted(name)

    def key_in_table(self, name, sqlkey):  #
        """:return: True if key exists, else false"""
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

    def put_in_stockdata(self, name, sqlkey, data):  #
        """ properly formatted and ready to insert into stockdata.db
        :param data: list of 390 reals
        :return: True if inserted, False if already exists"""
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

    def table_exists(self, tablename):  #
        """Ensures the table exist from the onRecord table.
        :return: True if table exists, else False"""
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

    def create_table(self, name):  #
        """:return: True if successful, False else"""
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

    def remove_table(self, name): #
        """tableflip.jpg :param name: ticker"""
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
