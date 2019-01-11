# Owner-Alexander Kern, Freddy Cervantes
# This project is open to anyone

# Dependencies

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from iexfinance.stocks import get_historical_data
import occasion


class StockDev:

    def __init__(self, ticker):
        self.__state = True
        self.__ticker = ticker
        self.__m = 0
        self.__b = 0
        self.__std = 0
        self.__todayPrice = 0
        self.__y = []
        self.__numDays = 0
        self.__dates = []
        self.__std_from_mean = 0
        self.__find_linear_function(self)
        self.__find_standard_deviation_from_mean()

    def get_dev_from_mean(self):
        return abs(self.__std_from_mean)

    def __find_standard_deviation_from_mean(self):
        frommean = self.__y[self.__numDays - 1] - (len(self.__y) - 1) * self.__m - self.__b
        self.__std_from_mean = frommean / self.__std

    def say_state(self):
        print("The current linear line is y = {}x + {}, and the standard deviation is {}".format(self.__m, self.__b, self.__std))

    def exists(self):
        return self.__state

    def return_state(self):
        frommean = self.__y[self.__numDays - 1] - (len(self.__y) - 1) * self.__m - self.__b
        frommean = frommean / self.__std
        return "{}: \n\n" \
               "todays price: ${}\n\n" \
               "price is {} deviation/s from the 5 year linear mean".format(
            self.__ticker, self.__todayPrice, frommean)

    def todays_deviation(self):
        frommean = self.__y[self.__numDays - 1] - (len(self.__y) - 1) * self.__m - self.__b
        frommean = frommean / self.__std
        print("std: {}, price {} at {} deviation/s from the mean".format(
              self.__std, list(self.__dates)[self.__numDays - 1], frommean))
        if abs(frommean) > 1:
            return True
        return False

    # Finds historical data for the spx from today to 5 years ago
    @staticmethod
    def __find_linear_function(self):
        start, end = self.__get_dates_5year()
        # Make array for "y" outputs
        y = self.__logy_outputs(self, start, end)
        self.__linear_coefficents(self, list(y))
        self.__find_standard_deviation(self, y)

    @staticmethod
    def __find_standard_deviation(self, y):
        y_prime = [i * self.__m + self.__b for i in range(len(y))]
        # SD = sqrt( [sum(y - y')/(n-2)]  )
        y_sum = sum([(y[i] - y_prime[i]) ** 2 for i in range(len(y))]) / (len(y) - 2.0)
        self.__std = sqrt(y_sum)

    # Ax=b, A^T*Ax=A^T*b, x=(A^T*A)^-1*A^T*b
    @staticmethod
    def __linear_coefficents(self, b):
        A = np.array([[float(i), 1.0] for i in range(len(b))])
        b = A.T.dot(np.array(b))
        A = A.T.dot(A)
        b = np.linalg.inv(A).dot(b)
        self.__m = b[0]
        self.__b = b[1]

    @staticmethod
    def __get_dates_5year():
        return occasion.Occasion().five_years()

    @staticmethod
    def __logy_outputs(self, start, end):
        try:
            data = get_historical_data(self.__ticker, start, end)
        except:
            print("{} is not availible or does not exist".format(self.__ticker))
            data = {"key1": {'close': 1}, "key2": {'close': 2},"key3": {'close': 4},}
            self.__state = False
        self.__dates = data.keys()
        y = []
        for i in data.keys():
            y += [data[i]['close']]
        self.__y = list(y)
        self.__numDays = len(y)
        self.__todayPrice = np.exp(y[self.__numDays - 1])
        return y

    def plot_with_dev(self):
        plt.close(1)
        plt.figure(1)
        plt.plot(self.__y, 'k')
        line = [i * self.__m + self.__b for i in range(self.__numDays)]
        # Blue is the line of regression
        # Green is 1 standard deviation
        # Red is 2 sd.
        plt.plot(line, 'b')
        plt.plot([i - self.__std for i in line], 'g')
        plt.plot([i + self.__std for i in line], 'g')
        plt.plot([i - self.__std * 2 for i in line], 'r')
        plt.plot([i + self.__std * 2 for i in line], 'r')
        plt.xticks(np.arange(0, self.__numDays, 250), [list(self.__dates)[i] for i in range(0, self.__numDays, 250)])
        plt.show()



if __name__ == '__main__':
    spy = StockDev("BBD")
    spy.say_state()
    print(spy.get_dev_from_mean())
    spy.plot_with_dev()

    print("welcome")
