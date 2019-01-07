class GetItems:
    def __init__(self):
        self.__stockKeys = {'SIRI': 'Sirus XM', 'DBX': 'DropBox', 'FB': 'Facebook',
                    'P': 'Pandora', 'BABA': 'Alibaba', 'TWTR': 'Twitter',
                    'ORCL': 'Oracle', 'WBA': 'Walgreens', 'NKE': 'Nike',
                    'MSFT': 'Microsoft', 'VXX': 'Volitility index', 'COKE': 'CocaCola',
                    'INTC': 'Intel', 'AAPL': 'Apple', 'CRM': 'SalesForce',
                    'AMD': 'Advanced Micro Devices', 'TSLA': 'Tesla', 'SPOT': 'Spotify',
                    'PYPL': 'Paypal', 'GOOGL': 'Google', 'SNAP': 'Snapchat',
                    'GPRO': 'Gopro', 'CSCO': 'Cisco', 'BAC': 'Bank of America',
                    'VZ': 'Verizon', 'WMT': 'Walmart', 'PG': 'Proctor and Gamble',
                    'NTNX': 'Nutanix', 'F': 'Ford', 'GS': 'Goldman Sacs', 'GM': 'General Moters',
                    'T': 'AT&T', 'SPXL': 'Large cap SPY', 'MU': 'MemeStock (Micron)',
                    'SPY': 'S&P', 'GE': 'General Electric', 'GIS': 'General Mills',
                    'AMZN': 'Amazon', 'ANET': 'Arista', 'PFE': 'Pfizer', 'SQ': 'Square(Finance)',
                    'MMM': 'Garbage', 'BA' : 'Boeing', 'CAT' : 'Caterpillar',
                    'AXP': 'American Express', 'V': 'Verizon', 'DWDP': 'DowDuPoint', 'PSEC': 'Prospect Capital',
                    'IBM': 'IBM', 'XOM': "Exxon Mobile", 'JPM': 'JPMorgan', 'UTX': 'United Technologies Corp',
                    'DIS': 'Disney', 'MRK': 'Merck & Co. Inc.', 'TRV': 'Travelers Cos. Inc.',
                    'HD': 'Home Depot', 'CVX': 'Cheveron', 'KO': 'Coka Cola', 'MCD': 'McHeartattacks',
                    'JNJ': 'Jhonson & Jhonson','UNH': 'UnitedHealth Group', 'K': 'Kellog', 'XRX': 'Xerox',
                    'RIG': "They drill the ocean" }

    def approved_stocks(self):
        """
        :return: List of approved stocks
        >>> x = GetItems()
        >>> 'VZ' in x.approved_stocks()
        True
        >>> 'VZZ' in x.approved_stocks()
        False
        """
        return list(self.__stockKeys.keys())

    def whitelisted(self, name):
        """
        :param name: Ticker
        :return: True if it is okay
        >>> x = GetItems()
        >>> x.whitelisted("VZ")
        True
        >>> x.whitelisted("VJLKJ")
        False
        """
        x = self.approved_stocks()
        return name in x


if __name__=="__main__":
    import doctest
    doctest.testmod()