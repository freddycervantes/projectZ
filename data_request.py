"""

"""


class GetData:

    def __init__(self):
        self.__update = self.__get_update()
        self.__organize = self.__get_organize()
        self.__whitelist = self.__get_whitelist()
        self.__stock_gen = self.__get_stock()
        self.__update_all_intraday()
        self.__stocks = {}

    @staticmethod
    def __get_stock():
        import stock
        return stock
    @staticmethod
    def __get_update():
        import update_database
        return update_database.Update()

    @staticmethod
    def __get_organize():
        import organize_data
        return organize_data.Organize()

    @staticmethod
    def __get_whitelist():
        import whitelist
        return [i for i in whitelist.GetItems().approved_stocks() if i != 'XRX']

    def __update_all_intraday(self):
        """
        Updates All intraday stocks up to yesterday
        """
        self.__update.update_all()

    def __get_all_intraday(self, name):
        if name not in self.__whitelist:
            return False
        return self.__organize.all_intraday(name)

    def add_stock(self, name):
        if name not in self.__whitelist:
            return False
        self.__stocks[name] = self.__stock_gen.Stock(name, self.__get_all_intraday(name), [i**2 for i in range(10)])

    def get_stock(self, name):
        if name not in self.__stocks.keys():
            return False
        return self.__stocks[name]

    def add_all_stocks(self):
        """
        :param name: ticker
        :return: Stock() object
        note this tests add_stock and get_stock as well
        >>> G = GetData()
        >>> G.add_stock("NONEXIST")
        False
        >>> G.add_all_stocks()
        >>> G.get_stock("NONEXIST")
        False
        >>> spy = G.get_stock("SPY")
        >>> spy.name()
        'S&P'
        """
        for i in self.__whitelist:
            self.add_stock(i)



if __name__=="__main__":
    import doctest
    doctest.testmod()
