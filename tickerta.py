# Owner-Alexander Kern
# This project is open to anyone

# Dependencies

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from math import sqrt
from iexfinance.stocks import get_historical_data


class StockDev:

    def __init__(self, ticker):
        self.__ticker = ticker
        self.__m = 0
        self.__b = 0
        self.__std = 0
        self.__todayPrice = 0
        self.__logy = []
        self.__numDays = 0
        self.__dates = []
        self.__find_linear_function(self)

    def say_state(self):
        print("The current linear line is y = {}x + {}, and the standard deviation is {}".format(self.__m, self.__b,
                                                                                                 self.__std))

    def todays_deviation(self):
        frommean = self.__logy[self.__numDays - 1] - (len(self.__logy) - 1) * self.__m - self.__b
        frommean = frommean / self.__std
        print("std: {}, price {} at {} deviation/s from the mean".format(
              self.__std, list(self.__dates)[self.__numDays - 1], frommean))
        if abs(frommean) > 1:
            return True
        return False

    # Finds historical data for the spx from today to 5 years ago
    @staticmethod
    def __find_linear_function(self):
        start, end = self.__get_dates_5year(self)
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
    def __get_dates_5year(self):
        end = datetime.today()
        end = datetime(end.year + 1, 1, 1)
        start = datetime(end.year - 5, 1, 1)
        return start, end

    @staticmethod
    def __logy_outputs(self, start, end):
        try:
            data = get_historical_data(self.__ticker, start, end)
        except:
            print("{} is not availible or does not exist".format(self.__ticker))
            exit(2)
        self.__dates = data.keys()
        y = []
        for i in data.keys():
            y += [np.log(data[i]['close'])]
        self.__logy = list(y)
        self.__numDays = len(y)
        self.__todayPrice = y[self.__numDays - 1]
        return y

    def plot_with_dev(self):
        plt.close(1)
        plt.figure(1)
        plt.plot(self.__logy, 'k')
        line = [i * self.__m + self.__b for i in range(self.__numDays)]
        plt.plot(line, 'b')
        plt.plot([i - self.__std for i in line], 'g')
        plt.plot([i + self.__std for i in line], 'g')
        plt.plot([i - self.__std * 2 for i in line], 'r')
        plt.plot([i + self.__std * 2 for i in line], 'r')
        plt.xticks(np.arange(0, self.__numDays, 250), [list(self.__dates)[i] for i in range(0, self.__numDays, 250)])
        plt.show()




if __name__ == '__main__':
    spx = StockDev("SPY")
    spx.say_state()
    spx.plot_with_dev()
    print(spx.todays_deviation())