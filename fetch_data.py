"""
File for getting data from IEX finance
This will be the ONLY file where we import iexfinance
"""
import iexfinance as iex


def get_intraday_raw(name, date):
    """
    :param name: ticker
    :param date: datetime.datetime.(year, month, day)
    :return: list of raw data
    >>> 0 == 0
    True
    """
    return iex.stocks.get_historical_intraday(name, date)
def get_intraday_average_price(name, date):
    return [i['average'] for i in get_intraday_raw(name, date)]
def get_five_year(name):
    return None

if __name__=="__main__":
    import doctest
    doctest.testmod()