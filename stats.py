"""

"""

class Stats:

    def __init__(self):
        self.__whitelist = None
        self.__data = self.__get_data_request()

    def __get_data_request(self):
        import data_request
        d = data_request.GetData()
        self.__whitelist = d.get_whitelist()
        return d

if __name__=="__main__":
    import doctest
    doctest.testmod()
