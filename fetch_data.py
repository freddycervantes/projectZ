"""
File for getting data from IEX finance
This will be the ONLY file where we import iexfinance
"""
import iexfinance as iex
import occasion
class Fetch:

    def __init__(self):
        self.__iex = self.__get_iex()

    def __get_iex(self):
        import iexfinance
        return iexfinance

def get_intraday_raw(name, date):
    """
    need to update price every 3 months
    :param name: ticker
    :param date: datetime.datetime.(year, month, day)
    :return: list of raw data
    >>> import datetime
    >>> get_intraday_raw("SPY", datetime.datetime(2019, 1, 3))[0]['date']
    '20190103'
    """
    return iex.stocks.get_historical_intraday(name, date)


def intraday_volume(name, date):
    """
    need to update tests every 3 months
    :param name: ticker
    :param date: datetime.datetime.(year, month, day)
    :return: list of volumes for a given min
    >>> from datetime import datetime
    >>> intraday_volume("SPY", datetime(2019, 1, 3))[0]
    3759
    """
    return [i['volume'] for i in get_intraday_raw(name, date)]


def intraday_average_price(name, date):
    """
    need to update tests every 3 months
    :return: list of average prices per minute
    >>> from datetime import datetime
    >>> intraday_average_price("SPY", datetime(2019, 1, 3))[0]
    248.407
    """
    return [i['average'] for i in get_intraday_raw(name, date)]


def get_five_year_raw(name):
    """
    HTF DO YOU TEST THIS??!!
    :param name:
    :return:
    >>> 0==0
    True
    """
    start, end = occasion.five_years()
    return iex.stocks.get_historical_data(name, start, end)


if __name__=="__main__":
    import doctest
    doctest.testmod()
