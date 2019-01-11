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

    def get_intraday_raw(self, name, date):  #
        """need to update price every 3 months
        :param name: ticker
        :param date: datetime.datetime.(year, month, day)
        :return: list of raw data"""
        return self.__iex.stocks.get_historical_intraday(name, date)

    def intraday_volume(self, name, date):  #
        """:param date: datetime.datetime.(year, month, day)
        :return: list of volumes for a given min"""
        return [i['volume'] for i in self.get_intraday_raw(name, date)]

    def intraday_average_price(self, name, date):  #
        """:return: list of average prices per minute"""
        return [i['average'] for i in self.get_intraday_raw(name, date)]

    def get_raw_days(self, name, start, end):
        return self.__iex.stocks.get_historical_data(name, start, end)

    def get_five_year_raw(self, name):
        """raw 5 year data"""
        start, end = self.__date_tool.five_years()
        return self.__iex.stocks.get_historical_data(name, start, end)

    def five_year_dates(self, name):
        """
        :param name: Ticker
        :return: list of datetime.datetime(year, month, day)'s

        """
        raw = list(self.get_five_year_raw(name).keys())
        return [self.__date_tool.get_date(int(i[0:4]), int(i[5:7]), int(i[8:10])) for i in raw]

    def list_valid_intraday_dates(self):  #
        """:return: List of valid intraday dates
        Binary search for smallest dates possible"""
        lis = self.five_year_dates("SPY")
        lis = lis[len(lis) - 129:]
        min_date_index = 128
        curr_index = 64
        add_sub = 32
        while add_sub >= 0.9:
            if self.vaild_intraday_day("SPY", lis[curr_index]):     # Binary search method
                min_date_index = curr_index
                curr_index -= int(add_sub)
            else:
                curr_index += int(add_sub)
            add_sub /= 2
        if self.vaild_intraday_day("SPY", lis[curr_index]):         # Checks the tail case
            min_date_index = curr_index
        if self.__date_tool.today() in lis:
            lis.remove(self.__date_tool.today())
        return lis[min_date_index:]

    def vaild_intraday_day(self,name, day):  #
        """:return: true if day is on record"""
        return self.__iex.stocks.get_historical_intraday(name, day) != []



if __name__=="__main__":
    import doctest
    doctest.testmod()
