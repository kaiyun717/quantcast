"""
Quantcast - Coding challenge
Author: Kai Yun
"""
import os
import sys
import re
import argparse
import datetime


def return_most_active_cookie(file_name, date):
    """ Returns the most active cookie for the given date from a cookie log file.
    (Most active cookie is defined as one seen in the log the most times during
     a given day.)

    Args:
        file_name: the name of the cookie log csv file
        date: the date in which the most active cookie is searched

    Returns:
        The most active cookie.

    Example usage
        Given a cookie log file in csv format:
        $ cat cookie_log.csv
        cookie,timestamp
        AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
        SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
        5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
        AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
        SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
        4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
        fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
        4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
        
        >>> most_active_cookie(cookie_log.csv, 2018-12-09)
        >>> AtY0laUfhglK3lC7
    
    """
    

    print(file_name, date)


def proper_file_name(file_name):
    """Returns the file name if its format is proper. Otherwise raise error."""
    if file_name[-4:] != ".csv":
        msg = "{file_name} is not a proper csv file name.".format(file_name=file_name)
        raise argparse.ArgumentTypeError(msg)

    return file_name

def proper_date(date):
    """Returns the date if its format is proper. Otherwise raise error."""
    date_pattern = r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'
    if not bool(re.match(date_pattern, date)):
        msg = "{date} has to be in the format YYYY-MM-DD.".format(date=date)
        raise argparse.ArgumentTypeError(msg)
    
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    today_date = datetime.date.today()
    if today_date < datetime.datetime(year, month, day).date():
        msg = "{date} has to be a date up to today.".format(date=date)
        raise argparse.ArgumentTypeError(msg)
    
    return date

def main(file_name, date):
    most_active_cookie = return_most_active_cookie(file_name=file_name,
                                                   date=date)
    print(most_active_cookie)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=proper_file_name,
                        help='the name of the cookie log csv file to be searched')
    parser.add_argument('-d', '--date', type=proper_date,
                        help='date in which the most active cookie is searched',
                        required=True)
    args = parser.parse_args()
    
    main(file_name=args.file, date=args.date)
