
"""
This file is purely for testing, ensuring all test cases are working.
"""


def test_format():
    """
    :return: None
    >>> from format import Format
    >>> t = Format()
    >>> import occasion
    >>> O = occasion.Occasion()

    >>> t.write_date(O.get_date(1999,12,31))                # Format write_date
    19991231
    >>> name = "SPX"
    >>> sqlkey = 12345
    >>> data = [1.0, 2.0, 3.0]
    >>> t.write_intraday_data(name, sqlkey, data)           # Format write_intraday_data
    'INSERT INTO SPX VALUES (12345, 1.0, 2.0, 3.0)'
    >>> t.write_intraday_table("test")                      # Format write_intraday_table
    "CREATE TABLE test (date INT PRIMARY KEY, '0' real, '1' real, '2' real, '3' real, '4' real, '5' real, '6' real, '7' real, '8' real, '9' real, '10' real, '11' real, '12' real, '13' real, '14' real, '15' real, '16' real, '17' real, '18' real, '19' real, '20' real, '21' real, '22' real, '23' real, '24' real, '25' real, '26' real, '27' real, '28' real, '29' real, '30' real, '31' real, '32' real, '33' real, '34' real, '35' real, '36' real, '37' real, '38' real, '39' real, '40' real, '41' real, '42' real, '43' real, '44' real, '45' real, '46' real, '47' real, '48' real, '49' real, '50' real, '51' real, '52' real, '53' real, '54' real, '55' real, '56' real, '57' real, '58' real, '59' real, '60' real, '61' real, '62' real, '63' real, '64' real, '65' real, '66' real, '67' real, '68' real, '69' real, '70' real, '71' real, '72' real, '73' real, '74' real, '75' real, '76' real, '77' real, '78' real, '79' real, '80' real, '81' real, '82' real, '83' real, '84' real, '85' real, '86' real, '87' real, '88' real, '89' real, '90' real, '91' real, '92' real, '93' real, '94' real, '95' real, '96' real, '97' real, '98' real, '99' real, '100' real, '101' real, '102' real, '103' real, '104' real, '105' real, '106' real, '107' real, '108' real, '109' real, '110' real, '111' real, '112' real, '113' real, '114' real, '115' real, '116' real, '117' real, '118' real, '119' real, '120' real, '121' real, '122' real, '123' real, '124' real, '125' real, '126' real, '127' real, '128' real, '129' real, '130' real, '131' real, '132' real, '133' real, '134' real, '135' real, '136' real, '137' real, '138' real, '139' real, '140' real, '141' real, '142' real, '143' real, '144' real, '145' real, '146' real, '147' real, '148' real, '149' real, '150' real, '151' real, '152' real, '153' real, '154' real, '155' real, '156' real, '157' real, '158' real, '159' real, '160' real, '161' real, '162' real, '163' real, '164' real, '165' real, '166' real, '167' real, '168' real, '169' real, '170' real, '171' real, '172' real, '173' real, '174' real, '175' real, '176' real, '177' real, '178' real, '179' real, '180' real, '181' real, '182' real, '183' real, '184' real, '185' real, '186' real, '187' real, '188' real, '189' real, '190' real, '191' real, '192' real, '193' real, '194' real, '195' real, '196' real, '197' real, '198' real, '199' real, '200' real, '201' real, '202' real, '203' real, '204' real, '205' real, '206' real, '207' real, '208' real, '209' real, '210' real, '211' real, '212' real, '213' real, '214' real, '215' real, '216' real, '217' real, '218' real, '219' real, '220' real, '221' real, '222' real, '223' real, '224' real, '225' real, '226' real, '227' real, '228' real, '229' real, '230' real, '231' real, '232' real, '233' real, '234' real, '235' real, '236' real, '237' real, '238' real, '239' real, '240' real, '241' real, '242' real, '243' real, '244' real, '245' real, '246' real, '247' real, '248' real, '249' real, '250' real, '251' real, '252' real, '253' real, '254' real, '255' real, '256' real, '257' real, '258' real, '259' real, '260' real, '261' real, '262' real, '263' real, '264' real, '265' real, '266' real, '267' real, '268' real, '269' real, '270' real, '271' real, '272' real, '273' real, '274' real, '275' real, '276' real, '277' real, '278' real, '279' real, '280' real, '281' real, '282' real, '283' real, '284' real, '285' real, '286' real, '287' real, '288' real, '289' real, '290' real, '291' real, '292' real, '293' real, '294' real, '295' real, '296' real, '297' real, '298' real, '299' real, '300' real, '301' real, '302' real, '303' real, '304' real, '305' real, '306' real, '307' real, '308' real, '309' real, '310' real, '311' real, '312' real, '313' real, '314' real, '315' real, '316' real, '317' real, '318' real, '319' real, '320' real, '321' real, '322' real, '323' real, '324' real, '325' real, '326' real, '327' real, '328' real, '329' real, '330' real, '331' real, '332' real, '333' real, '334' real, '335' real, '336' real, '337' real, '338' real, '339' real, '340' real, '341' real, '342' real, '343' real, '344' real, '345' real, '346' real, '347' real, '348' real, '349' real, '350' real, '351' real, '352' real, '353' real, '354' real, '355' real, '356' real, '357' real, '358' real, '359' real, '360' real, '361' real, '362' real, '363' real, '364' real, '365' real, '366' real, '367' real, '368' real, '369' real, '370' real, '371' real, '372' real, '373' real, '374' real, '375' real, '376' real, '377' real, '378' real, '379' real, '380' real, '381' real, '382' real, '383' real, '384' real, '385' real, '386' real, '387' real, '388' real, '389' real)"
    >>> t.read_intraday_table_select_dates("SPY", t.write_date(O.get_date(2018, 12, 15)),
    ...             t.write_date(O.get_date(2019, 1, 1)))   # Format read_intraday_table
    'SELECT * FROM SPY WHERE date >= 20181215 AND date < 20190101 ORDER BY date'
    >>> t.read_intraday_table_select_dates("SPY", t.write_date(O.get_date(2018, 12, 15)),
    ...             t.write_date(O.get_date(2017, 1, 1)))   # Dates out of order, return False
    False
    >>> t.read_intraday_table_all("SPY")                    # Format read_intraday_table
    'SELECT * FROM SPY ORDER BY date'
    """
    return


def test_stock():
    """
    >>> from stock import Stock
    >>> tick = Stock("SPY", [i**2 for i in range(10)], [i**2 for i in range(10)])
    >>> tick.five_year_b()                              # Stock five_year_b
    -12.0
    >>> tock = Stock("TEST", [i**2 for i in range(1)], [i**2 for i in range(1)])
    >>> tock.five_year_b()
    0.0
    >>> tick.five_year_m()                              # Stock five_year_m
    -12.0
    >>> tock.five_year_m()                              # Stock five_year_m
    0.0
    >>> int(tick.five_std()*100000)/100000.0            # Stock five_std
    8.12403
    >>> tock.five_std()
    0.0
    >>> int(tick.five_std_from_mean()*100000)/100000.0  # Stock five_std_from_mean
    1.47709
    >>> tock.five_std_from_mean()
    0.0
    >>> tick.intraday_b()                               # Stock intraday_b
    -12.0
    >>> tock.intraday_b()
    0.0
    >>> tick.intraday_m()                               # Stock intraday_m
    9.0
    >>> tock.intraday_m()
    0.0
    >>> tick.intraday_data()                            # Stock intraday_data
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> tick.five_data()                                # Stock five_data
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> tick.name()                                     # Stock name
    'S&P'
    >>> tock.name()
    'TEST'
    >>> tick.curr_price()                               # Stock curr_price
    81
    >>> int(tick.intraday_std_from_mean()*100000)/100000.0
    1.47709
    >>> tock.intraday_std_from_mean()                   # Stock intraday_std_from_mean ^^las call was this too
    0.0
    >>> int(tick.intraday_std()*100000)/100000.0        # Stock intraday_std
    8.12403
    >>> tock.intraday_std()
    0.0
    """
    return None


def test_occastion():
    """
    >>> from occasion import Occasion
    >>> O = Occasion()
    >>> O.get_date(1987, 7, 28)             # Occasion get_date
    datetime.datetime(1987, 7, 28, 0, 0)
    >>> Occasion().today().year             # Occasion today
    2019
    >>> x = O.five_years()                  # Occasion five_years
    >>> x[0].year
    2014
    >>> x[1].year
    2019
    >>> x = O.ninedy_days()                 # Occasion ninedy_days
    >>> x[0].year*10000 + x[0].month*100 + x[0].day <  x[89].year*10000 + x[89].month*100 + x[89].day
    True
    >>> O.today() == x[89]
    True
    """
    return None


def test_write_dat():
    """
    >>> import occasion
    >>> ticker = "SPY"
    >>> date = occasion.Occasion().get_date(2019,1,3)
    >>> from write_dat import Write
    >>> t = Write()
    >>> t.day_in_database(date, ticker)                         # Write day_in_database
    True
    >>> t.day_in_database(occasion.Occasion().get_date(1999, 12, 31), ticker) # Y2K IS NEIGH
    False
    >>> from iexfinance.stocks import get_historical_intraday
    >>> x = [i['average'] for i in get_historical_intraday(ticker, date)]
    >>> t.store3(ticker, date, x)                               # Write store3
    False
    >>> ticker = "XRX"
    >>> x = [i['average'] for i in get_historical_intraday(ticker, date)]
    >>> t.store3(ticker, date, x)
    True
    >>> t.store3(ticker, date, [])
    False
    >>> t.table_exists(ticker)
    True
    >>> t.remove_table(ticker)                                  # Write remove_table, table exists
    >>> t.table_exists(ticker)
    False
    >>> t.store3(ticker, date, [1])
    True
    >>> t.remove_table(ticker)
    >>> Write.in_whitelist("GE")                                # Write in_whitelist
    True
    >>> Write.in_whitelist("SPX")
    False
    >>> t.key_in_table("SPX", 19991231)                         # Write key_in_table
    False
    >>> t.put_in_stockdata("SPX", 19991231, [i for i in range(390)])
    True
    >>> t.key_in_table("SPX", 19991231)
    True
    >>> t.key_in_table("SPX", 19991232)
    False
    >>> t.remove_table("SPX")
    >>> t.table_exists("SPX")                                   # Write put_in_stockdata
    False
    >>> t.put_in_stockdata("SPX", 19991231,[i for i in range(390)])
    True
    >>> t.table_exists("SPX")
    True
    >>> t.put_in_stockdata("SPX", 19991231,[i for i in range(390)])
    False
    >>> t.put_in_stockdata("SPX", 19991232,[i for i in range(390)])
    True
    >>> t.remove_table("SPX")                                   # Write create_table
    >>> t.create_table("SPX")
    True
    >>> t.create_table("SPX")
    False
    >>> t.remove_table("SPX")
    """
    return None


def test_whitelist():
    """
    >>> from whitelist import GetItems
    >>> x = GetItems()
    >>> x.whitelisted("VZ")                 # GetItems whitelisted
    True
    >>> x.whitelisted("TEST")
    False
    >>> 'VZ' in x.approved_stocks()         # GetItems approved_stocks
    True
    >>> 'VZZ' in x.approved_stocks()
    False
    >>> x.get_name("SPY")                   # GetItems get_name
    'S&P'
    >>> x.get_name("FLOOD")
    False
    """
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
