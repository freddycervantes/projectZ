"""

"""


class Stock:

    def __init__(self, ticker, intraday_data, five_year_data):
        # stock specs
        self.__whitelist = self.__get_whitelist()
        self.__np = self.__get_numpy()
        self.__ticker = ticker
        self.__curr_price = intraday_data[len(intraday_data) - 1]
        self.__vol = [i[2] for i in five_year_data]
        self.__dates = [i[0] for i in five_year_data]

        # intraday specs
        self.__intraday_data = intraday_data
        self.__intra_data_count = len(self.__intraday_data)
        self.__intra_m, self.__intra_b = self.__linear_coefficents(self.__intraday_data)
        self.__intra_sd, self.__intra_from_mean = self.__find_standard_deviation(self.__intra_m,
                                                                                 self.__intra_b, self.__intraday_data)

        # five year specs
        self.__five_year_data = [i[1] for i in five_year_data]
        self.__five_data_count = len(self.__five_year_data)
        self.__five_m, self.__five_b = self.__linear_coefficents(self.__five_year_data)
        self.__five_sd, self.__five_from_mean = self.__find_standard_deviation(self.__five_m,
                                                                               self.__five_b, self.__five_year_data)

    @staticmethod
    def __get_numpy():
        import numpy
        return numpy

    def __linear_coefficents(self, y):
        if len(y) < 3:
            return 0.0, 0.0
        a = self.__np.array([[float(i), 1.0] for i in range(len(y))])
        b = a.T.dot(self.__np.array(y))
        a = a.T.dot(a)
        b = self.__np.linalg.inv(a).dot(b)
        return b[0], b[1]  # return m, b

    @staticmethod
    def __find_standard_deviation(m, b, data):
        from math import sqrt
        size = len(data)
        if size < 3:  # no divide by zero
            return 0.0, 0.0
        y_prime = [i * m + b for i in range(size)]
        # SD = sqrt( [sum(y - y')/(n-2)]  )
        y_sum = sum([(data[i] - y_prime[i]) ** 2 for i in range(size)]) / (size - 2.0)
        last_close_price = data[size - 1]
        dev_from_mean = last_close_price - ((size - 1) * m + b)
        standard_dev = sqrt(y_sum)
        dev_from_mean = dev_from_mean / standard_dev
        return standard_dev, dev_from_mean

    @staticmethod
    def __get_whitelist():
        import whitelist
        return whitelist.GetItems()

    def curr_price(self):  #
        return self.__curr_price

    def name(self):  #
        """:return: name if in whitelist, else just ticker"""
        if  self.__ticker not in self.__whitelist.approved_stocks():
            return self.__ticker
        return self.__whitelist.get_name(self.__ticker)

    # Five year functions
    ##############################################################################################
    def five_volume(self):  #
        """:return: list of 5 year vol"""
        return self.__vol

    def five_dates(self):
        """:return: ordered dates"""
        return self.__dates

    def five_data(self):  #
        """:return: list of 5 year data"""
        return self.__five_year_data

    def five_std_from_mean(self):  #
        """:return: current price minus the line divided by std"""
        return self.__five_from_mean

    def five_std(self):  #
        """:return: standard deviation of all data from line"""
        return self.__five_sd

    def five_year_m(self):  #
        """:return: x coefficent"""
        return self.__five_b

    def five_year_b(self):  #
        """:return: y = mx + it b like that sometimes"""
        return self.__five_b

    ##############################################################################################

    # Intraday funcs
    ##############################################################################################
    def intraday_data(self):  #
        """:return: list of intraday data"""
        return self.__intraday_data

    def intraday_std_from_mean(self): #
        """:return: how many standard deviations from the mean"""
        return self.__intra_from_mean

    def intraday_std(self):  #
        """:return: intra standard deviation"""
        return self.__intra_sd

    def intraday_m(self):  #
        """:return: x coefficient intraday"""
        return self.__intra_m

    def intraday_b(self):  #
        """:return: y = mx intraday b"""
        return self.__intra_b
    ##############################################################################################


if __name__ == "__main__":
    import doctest
    doctest.testmod()
