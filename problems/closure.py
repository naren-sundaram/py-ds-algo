from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


class InvalidTimestampOption(Exception):
    pass


def range_timestamp(opt='1h'):
    """
    :param: opt shall be in (1h, 1d, 1w, 1m, 3m)
    :returns: from and to timestamps based on opt input
    :rtype: tuple(timestamp, timestamp)
    """
    measures = {'h': 'hours', 'd': 'days', 'w': 'weeks', 'm': 'months'}
    if len(opt) != 2 or opt[1] not in measures.keys() or not opt[0].isdigit():
        raise InvalidTimestampOption("Invalid Timestamp Option!")
    value, measure, now = int(opt[0]), opt[1], dt.now()
    kwargs = {measures[measure]: -value}
    return now.timestamp(), (now + rd(**kwargs)).timestamp()


# Testing with all possible inputs
options = ('1h', '1d', '1w', '1m', '3m')
for option in options:
    tsf, tst = range_timestamp(option)
    print("{}: ({}, {})".format(
        option,
        dt.fromtimestamp(tsf).strftime('%d-%m-%Y %H:%M:%S'),
        dt.fromtimestamp(tst).strftime('%d-%m-%Y %H:%M:%S')
    ))
