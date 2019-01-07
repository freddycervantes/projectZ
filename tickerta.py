# Owner-Alexander Kern, Freddy Cervantes
# This project is open to anyone

# Dependencies

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class StockDev:

    def __init__(self, ticker):
        self.__state = True
        self.__ticker = ticker
        self.__R = self.__import_read()
        self.__m = 0
        self.__b = 0
        self.__y = []
        self.__num_data_points = 0
        self.__standard_dev = 0
        self.__dev_from_mean = 0
        self.__approve = self.__import_whitelist_()
        self.__find_linear_function(self.__ticker)

    def get_dev_from_mean(self):

        return abs(self.__dev_from_mean)

    def plot_with_dev(self):
        plt.close(1)
        plt.figure(1)
        plt.plot(self.__y, 'k')
        line = [i * self.__m + self.__b for i in range(self.__num_data_points)]
        # Blue is the line of regression
        # Green is 1 standard deviation
        # Red is 2 sd.
        plt.plot(line, 'b')
        plt.plot([i - self.__standard_dev for i in line], 'g')
        plt.plot([i + self.__standard_dev  for i in line], 'g')
        plt.plot([i - self.__standard_dev  * 2 for i in line], 'r')
        plt.plot([i + self.__standard_dev * 2 for i in line], 'r')
        plt.show()

    def say_state(self):
        print("The current linear line is y = {}x + {}, and the standard deviation is {}".format(self.__m,
                                                                                self.__b, self.__standard_dev))
        print("Deviations from the mean: {}".format(self.__dev_from_mean))

    def __import_read(self):
        import read_db
        return read_db.Read()

    def __import_whitelist_(self):
        import whitelist
        return whitelist.GetItems().approved_stocks()

    def __find_linear_function(self, name):
        # Make array for "y" outputs
        self.__y_outputs(name)
        self.__linear_coefficents()
        self.__find_standard_deviation()

    def __find_standard_deviation(self):
        y_prime = [i * self.__m + self.__b for i in range(self.__num_data_points)]
        # SD = sqrt( [sum(y - y')/(n-2)]  )
        y_sum = sum([(self.__y[i] - y_prime[i]) ** 2 for i in range(self.__num_data_points)]) / \
                (self.__num_data_points - 2.0)
        last_close_price = self.__y[self.__num_data_points - 1]
        self.__dev_from_mean = last_close_price - ((self.__num_data_points - 2) * self.__m + self.__b)
        self.__standard_dev = sqrt(y_sum)
        self.__dev_from_mean = self.__dev_from_mean / self.__standard_dev

    # Ax=b, A^T*Ax=A^T*b, x=(A^T*A)^-1*A^T*b
    def __linear_coefficents(self):
        A = np.array([[float(i), 1.0] for i in range(self.__num_data_points)])
        b = A.T.dot(np.array(self.__y))
        A = A.T.dot(A)
        b = np.linalg.inv(A).dot(b)
        self.__m = b[0]
        self.__b = b[1]

    def __y_outputs(self, name):
        self.__y = self.__R.read_all(name)
        self.__num_data_points = len(self.__y)


if __name__ == '__main__':

    spy = StockDev("BAC")
    spy.say_state()
    spy.plot_with_dev()
    print("welcome")

