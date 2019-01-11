"""

"""

class Update:

    def __init__(self):
        self.__F = self.__fetch()
        self.__W = self.__write()
        self.__intra_dates = self.__valid_dates_intra()
        self.__stock_list = self.__valid_stocks()

    def __fetch(self):
        import fetch_data
        return fetch_data.Fetch()

    def __write(self):
        import write_dat
        return write_dat.Write()

    def __valid_stocks(self):
        import whitelist
        return whitelist.GetItems().approved_stocks()


    def __valid_dates_intra(self):
        return self.__F.list_valid_intraday_dates()

    def update_intra_single(self, name):
        """
        :param name:
        :return: False if not a valid stock, else true
        >>> U = Update()
        >>> U.update_intra_single("SPY")
        True
        >>> U.update_intra_single("SLDKHF")
        False
        """
        if name not in self.__stock_list:
            return False
        for i in reversed(self.__intra_dates):
            if self.__W.day_in_database(i, name):
                return True
            print(self.__W.store3(name, i, self.__F.intraday_average_price(name, i)))
            print(name)
        return True

    def update_5_single(self, name):
        if name not in self.__stock_list:
            return False
        self.__W.store5(name)
        return True

    def update_all(self):
        """
        >>> U = Update()
        >>> U.update_all()
        """
        for i in self.__stock_list:
            if i == 'XRX':
                continue
            self.update_intra_single(i)
            self.update_5_single(i)


if __name__=="__main__":
    import doctest
    doctest.testmod()