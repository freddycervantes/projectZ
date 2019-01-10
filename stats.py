"""

"""


class Stats:

    def __init__(self):
        self.__whitelist = None
        self.__data = self.__get_data_request()
        self.__stock_map = {}
        self.__intra_std_from_mean_list = []

    def __get_data_request(self):
        import data_request
        d = data_request.GetData()
        self.__whitelist = d.whitelist()
        return d



    def import_ticker(self, name):
        """
        :param name: ticker
        :return: False if not in whitelist, else None
        #>>> S = Stats()
        #>>> S.import_ticker("FRED")
        False
        #>>> S.import_ticker("SPY")
        """
        if name not in self.__whitelist:
            return False
        self.__data.add_stock(name)
        self.__update_stock(name)

    def import_all_stocks(self):
        """
        >>> S = Stats()
        >>> S.import_all_stocks()
        >>> S.print_10_smallest()
        """
        self.__data.add_all_stocks()
        for i in self.__whitelist:
            self.__update_stock(i)
        for i in self.__whitelist:
            ticker = self.__stock_map[i]
            self.__intra_std_from_mean_list += [(i,ticker['intra_fm'])]
        self.__intra_std_from_mean_list = sorted(self.__intra_std_from_mean_list, key=lambda k: k[1])

    def print_10_smallest(self):
        if len(self.__intra_std_from_mean_list) < 10:
            print(self.__intra_std_from_mean_list)
        else:
            print(self.__intra_std_from_mean_list[:10])

    def __update_stock(self, name):
        stock = self.__data.get_stock(name)

        temp = {
            'price'     : stock.curr_price(),
            'intra_sd'  : stock.intraday_std(),
            'intra_m'   : stock.intraday_m(),
            'intra_fm'  : stock.intraday_std_from_mean(),
            'intra_b'   : stock.intraday_b(),
            'five_sd'   : stock.five_std(),
            'five_m'    : stock.five_year_m(),
            'five_fm'   : stock.five_std_from_mean(),
            'five_b'    : stock.five_year_b()
        }
        self.__stock_map[name] = temp


if __name__ == "__main__":
    import doctest
    doctest.testmod()
