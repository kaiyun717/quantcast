"""
Quantcast - Coding challenge
Unit Tests
Author: Kai Yun
"""
import unittest
import sys
import os
import datetime
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.quantcast.most_active_cookie import return_most_active_cookies, \
                                         proper_date, \
                                         proper_file_name, \
                                         parse_args

 
class TestParseArgs(unittest.TestCase):
    def test_proper_date_type(self):
        date = '2019-01-13'
        date_returned = proper_date(date)
        self.assertIsInstance(date_returned, datetime.date)

    def test_improper_date_format_errors(self):
        wrong_dates = ['1000-20-01', '2030-10-01', '2020/10/01', '2001.01.21',
                       '0001-10.10', '2020-13-12', '2023-12-31', '01-21-2022']
        for date in wrong_dates:
            with self.assertRaises(argparse.ArgumentTypeError, 
                                   msg=f"Check if {date} is indeed in proper format"):
                proper_date(date)

    def test_proper_file_name(self):
        file_names = ['hello.csv', '/hello.csv', 'root/sub/data.csv']
        for file_name in file_names:
            self.assertEqual(proper_file_name(file_name), file_name,
                             msg=f"Check if {file_name} is in proper format")
    
    def test_improper_file_name_errors(self):
        file_names = ['hello', '/hello.cvs', 'root/sub/data']
        for file_name in file_names:
            with self.assertRaises(argparse.ArgumentTypeError,
                                   msg=f"Check if '{file_name}' is indeed in proper format"):
                proper_file_name(file_name)

    def test_parse_args(self):
        sys_argv = ['cookies.csv', '-d', '2018-12-08']
        returned_args = parse_args(sys_argv)
        expected_args = ['cookies.csv', datetime.datetime.strptime('2018-12-08', '%Y-%m-%d').date()]
        self.assertEqual(returned_args.file, expected_args[0])
        self.assertEqual(returned_args.date, expected_args[1])


class TestReturnMostActiveCookies(unittest.TestCase):
    def test_nonexisting_date(self):
        test_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'cookie_log1.csv')
        test_date = datetime.datetime.strptime('2019-12-01', '%Y-%m-%d')
        with self.assertRaises(ValueError):
            return_most_active_cookies(test_file, test_date)
    
    def test_log1_file(self):
        test_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'cookie_log1.csv')
        test_dates_and_results = {'2018-12-09': ['AtY0laUfhglK3lC7'], 
                                  '2018-12-08': ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'],
                                  '2018-12-07': ['4sMM2LxV07bPJzwf']}
        for k, v in test_dates_and_results.items():
            test_date = datetime.datetime.strptime(k, '%Y-%m-%d').date()
            returned_cookies = return_most_active_cookies(test_file, test_date)
            self.assertCountEqual(returned_cookies, v)
    
    def test_log2_file(self):
        test_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'cookie_log2.csv')
        test_date = datetime.datetime.strptime('2018-12-09', '%Y-%m-%d').date()
        expected_cookies = ['SAZuXPGUrfbcn5UA']
        returned_cookies = return_most_active_cookies(test_file, test_date)
        self.assertCountEqual(returned_cookies, expected_cookies)

    def test_log3_file(self):
        test_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'cookie_log3.csv')
        test_date = datetime.datetime.strptime('2018-12-07', '%Y-%m-%d').date()
        expected_cookies = ['4sMM2LxV07bPJzwf']
        returned_cookies = return_most_active_cookies(test_file, test_date)
        self.assertCountEqual(returned_cookies, expected_cookies)


if __name__ == '__main__':
    unittest.main()