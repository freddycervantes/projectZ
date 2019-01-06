"""

"""

class Update:

    def __init__(self):
        self.__F = self.__fetch()

    def __fetch(self):
        import fetch_data
        return fetch_data.Fetch()

if __name__=="__main__":
    import doctest
    doctest.testmod()