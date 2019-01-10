"""
ONLY file that uses datetime. tip your waitress
"""


class Occasion:

    def __init__(self):
        self.__date = self.__import_datetime()
        self.__day_gen = self.__date.datetime

    @staticmethod
    def __import_datetime():
        import datetime
        return datetime

    def get_date(self, year, month, day):  #
        """
        :return: datetime.datetime(year, month, day)
        """
        return self.__day_gen(year, month, day)

    def today(self):  #
        """
        :return: todays date as a datetime object
        """
        today = self.__day_gen.today()
        return self.get_date(today.year, today.month, today.day)

    def five_years(self):  #
        """
        :return: date of today and a day 5 years ago
        """
        end = self.today()
        start = end - self.__date.timedelta(days=(365 * 5))
        return start, end

    def ninedy_days(self):  #
        """
        :return: list of 90 days acending
        """
        today = self.today()
        return list(reversed([today - self.__date.timedelta(days=i) for i in range(90)]))
