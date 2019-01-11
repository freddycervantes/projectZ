"""
If you need something to look like another thing, call me.
867-5309
"""

class Format:

    def __init__(self):
        self.__x = 5

    # Intraday fucntions
    #####################################################################################################
    def read_intraday_table_all(self, name): #
        """
        :param name: Ticker
        :return: FormatProper
        """
        return 'SELECT * FROM {} ORDER BY date'.format(name)

    def read_intraday_table_select_dates(self, name, start_day, end_day): #
        """
        :param name: ticker
        :param start_day: formatted datetime
        :param end_day:   formatted datetime
        :return: formatted to be pulled from database
        """
        if start_day >= end_day:
            return False
        return "SELECT * FROM {} WHERE date >= {} AND date < {} ORDER BY date".format(name, start_day, end_day)

    @staticmethod
    def write_intraday_table(name): #
        """
        Takes in name and formats it for sqlite table creation
        """
        new_table = "CREATE TABLE {} (date INT PRIMARY KEY, ".format(name)
        for i in range(390):
            new_table += "'{}' real, ".format(i)
        new_table = new_table[:len(new_table) - 2] + ")"
        return new_table

    @staticmethod
    def write_intraday_data(name, sqlkey, data): #
        """
        :param data: array of 390 reals
        :return: string properly formatted
        """
        s = "INSERT INTO {} VALUES ({}, ".format(name, sqlkey) + str(data).replace("[", "").replace("]", "") + ")"
        return s
    #####################################################################################################

    # Yearly fucntions
    #####################################################################################################
    @staticmethod
    def write_five_day(name, sqlkey, close, volume):  #
        """:return: Formatted for a single day entry on the sql tabl"""
        s = "INSERT INTO {} VALUES ({}, {}, {})".format(name, sqlkey, close, volume)
        return s

    @staticmethod
    def make_five_table(name):  #
        """:return: formated table with volume and price for each date"""
        return "CREATE TABLE {} (date INT PRIMARY KEY, close REAL, volume INT)".format(name)

    @staticmethod
    def read_five_all(name):
        return "SELECT * FROM {} ORDER BY date".format(name)

    # Other
    #####################################################################################################
    @staticmethod
    def write_date(date):  #
        """:date:      datetime.datetime(year, month, day)
        :return:    Integer with yearmonthday """
        return date.year*10000 + date.month*100 + date.day     # I like turtles

    @staticmethod
    def date_text_to_int(date):
        return int(date[:4])*10000 + int(date[5:7])*100 + int(date[8:])
