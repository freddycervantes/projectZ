"""
ONLY file that uses datetime. tip your waitress
"""

import datetime


def today():
    """
    :return: IDK test it yourself
    >>> today()
    datetime.datetime(2019, 1, 5, 0, 0)
    """
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day)


def five_years():
    now = today()
    return None


def ninedy_days():
    return None


if __name__=="__main__":
    import doctest
    doctest.testmod()
