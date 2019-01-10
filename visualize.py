"""
visualize the data
"""

class Visuals:

    def __init__(self):
        self.__plt = self.__get_mat_plot()
        self.__stats = self.__get_stats()

    def __get_mat_plot(self):
        import matplotlib.pyplot as plt
        return plt

    def __get_stats(self):
        import stats
        return stats.Stats()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
