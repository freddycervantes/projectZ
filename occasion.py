"""
ONLY file that uses datetime. tip your waitress
"""


class Occasion:

    def __init__(self):
        self.__date = self.__import_datetime()
        self.__day_gen = self.__date.datetime

    def __import_datetime(self):
        import datetime
        return datetime

    def get_date(self, year, month, day):
        """
        :return: datetime.datetime(year, month, day)
        >>> Occasion().get_date(1987, 7, 28)
        datetime.datetime(1987, 7, 28, 0, 0)
        """
        return self.__day_gen(year, month, day)


    def today(self):
        """
        :return: IDK test it yourself
        >>> Occasion().today().year
        2019
        """
        today = self.__day_gen.today()
        return self.get_date(today.year, today.month, today.day)

    def five_years(self):
        """
        :return: date of today and a day 5 years ago
        >>> x = Occasion()
        >>> x = x.five_years()
        >>> x[0].year
        2014
        >>> x[1].year
        2019
        """
        end = self.today()
        start = end - self.__date.timedelta(days=(365 * 5))
        return start, end

    def ninedy_days(self):
        """
        :return: list of days acending
        >>> y = Occasion()
        >>> x = y.ninedy_days()
        >>> x[0].year*10000 + x[0].month*100 + x[0].day <  x[89].year*10000 + x[89].month*100 + x[89].day
        True
        >>> y.today() in x
        True
        """
        today = self.today()
        return list(reversed([today - self.__date.timedelta(days=i) for i in range(90)]))


if __name__=="__main__":
    import doctest
    doctest.testmod()
