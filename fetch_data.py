"""
File for getting data from IEX finance
This will be the ONLY file where we import iexfinance
"""
class Fetch:

    def __init__(self):
        self.__iex = self.__get_iex()
        self.__date_tool = self.__get_occasion()

    def __get_iex(self):
        import iexfinance
        return iexfinance

    def __get_occasion(self):
        import occasion
        return occasion.Occasion()

    def get_intraday_raw(self, name, date):
        """
        need to update price every 3 months
        :param name: ticker
        :param date: datetime.datetime.(year, month, day)
        :return: list of raw data
        >>> import occasion
        >>> x = occasion.Occasion()
        >>> Fetch().get_intraday_raw("SPY", x.get_date(2019, 1, 3))[0]['date']
        '20190103'
        """
        return self.__iex.stocks.get_historical_intraday(name, date)


    def intraday_volume(self, name, date):
        """
        need to update tests every 3 months
        :param name: ticker
        :param date: datetime.datetime.(year, month, day)
        :return: list of volumes for a given min
        >>> import occasion
        >>> x = occasion.Occasion()
        >>> Fetch().intraday_volume("SPY", x.get_date(2019, 1, 3))[0]
        3759
        """
        return [i['volume'] for i in self.get_intraday_raw(name, date)]

    def intraday_average_price(self, name, date):
        """
        need to update tests every 3 months
        :return: list of average prices per minute
        >>> import occasion
        >>> x = occasion.Occasion()
        >>> Fetch().intraday_average_price("SPY", x.get_date(2019, 1, 3))[0]
        248.407
        """
        return [i['average'] for i in self.get_intraday_raw(name, date)]


    def get_five_year_raw(self, name):
        """
        HTF DO YOU TEST THIS??!!
        :param name:
        :return:
        >>> 0==0
        True
        """
        start, end = self.__date_tool.five_years()
        return self.__iex.stocks.get_historical_data(name, start, end)


if __name__=="__main__":
    import doctest
    doctest.testmod()
