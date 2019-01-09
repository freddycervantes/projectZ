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
                    'RIG': "Transocean Inc", 'C' : 'Citygroup', 'WFC': 'Wells Fargo', 'CMCSA': 'Comcast',
                    'ET': 'Energy Tranfer Corp', 'AKS': 'AK Steel', 'NVAX': 'Novavax Inc',
                    'DNR': 'Denbury Resorces', 'RF': 'Regions Financal Corp', 'HAL': 'Haliburton Co',
                    'AMAT': 'Applied Materials', 'ROKU': 'Roku Inc', 'OAS': 'Oasis Inc', 'ESV': 'Ensoc Pic',
                    'EBAY': 'Figure it out youself', 'MRO': 'Maraton Oil Corp', 'MS': 'Morgan Stanley',
                    'TSM': 'Tai Semi Manufacuring', 'QCOM': 'Qualcomm', 'MRVL': 'Marvell tech group',
                    'FCAU': 'Fiat Chrysler Automobiles N.V.', 'ZNGA': 'Zynga', 'AUY': 'Aumana Gold',
                    'KMI': 'Kinder Morgan', 'BBD': 'Banco bradesco', 'SBUX': 'Starbucks', 'S': 'Sprint',
                    'GME': 'Gamestop', 'MGM': 'Hotel and casino', 'IQ': 'Iqiyi Inc', 'EQT': 'EQT Corp',
                    'COG': 'Cabot Oil & Gas', 'HPE': 'Hewlett Pakard', 'TEVA': 'TEVA Pharmaceutical', 'HBAN': 'Huntington Bcshs',
                    'MAT': 'Mattel', 'Dal': 'Delta air line', 'EPD': 'Enterprise Product Partners', 'X': 'US Steel',
                    'PE': 'Parley Energy', 'LYG': 'Lloyds Banking', 'TAK': 'Takeda Pharm', 'NLY': 'Annaly Capital',
                    'FOXA': 'Fox Net', 'MO': 'Altria Gropu', 'RRC': 'Range Resoruces', 'KR': 'Kroger Co',
                    'CHK': 'Chesapeake energy', 'GRPN': 'Groupon'}

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

    def get_name(self, ticker):
        """
        :param ticker:
        :return: actual company name
        >>> G = GetItems()
        >>> G.get_name("SPY")
        'S&P'
        >>> G.get_name("FLOOD")
        False
        """
        if ticker not in self.__stockKeys.keys():
            return False
        return self.__stockKeys[ticker]


if __name__=="__main__":
    import doctest
    doctest.testmod()