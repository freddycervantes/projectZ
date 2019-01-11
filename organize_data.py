"""

"""

class Organize:

    def __init__(self):
        self.__read = self.__get_read()

    def __get_read(self):
        import read_db
        return read_db.Read()

    def all_intraday(self, name):
        return self.__read.read_all_intra(name)

    def all_5_year(self, name):
        return self.__read.read_all_five(name)
