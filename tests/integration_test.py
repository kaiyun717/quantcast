"""
Quantcast - Coding challenge
Integration Test
Author: Kai Yun
"""
import unittest
import sys
import os
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from quantcast.most_active_cookie import main


class TestIntegration(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, *kwargs)
        self.test_file_names = ['cookie_log1.csv', 'cookie_log2.csv', 'cookie_log3.csv']
        self.test_files = [os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
                           for file_name in self.test_file_names]

        self.test_dates_str = ['2018-12-09', '2018-12-08', '2018-12-07']

    def test_main_error(self):
        with self.assertRaises(ValueError):
            main([self.test_files[1], '-d', '2018-12-07'])

    def test_main_cookie1(self):
        test_dates_and_results = {'2018-12-09': ['AtY0laUfhglK3lC7'], 
                                  '2018-12-08': ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'],
                                  '2018-12-07': ['4sMM2LxV07bPJzwf']}

        for k, v in test_dates_and_results.items():
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            main([self.test_files[0], '-d', k])
            sys.stdout = sys.__stdout__
            expectedOutput = '\n'.join(v) + '\n'
            self.assertEqual(expectedOutput, capturedOutput.getvalue())

    def test_main_cookie3(self):
        test_dates_and_results = {'2018-12-09': ['AtY0laUfhglK3lC7'], 
                                  '2018-12-08': ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'],
                                  '2018-12-07': ['4sMM2LxV07bPJzwf']}
        
        for k, v in test_dates_and_results.items():
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            main([self.test_files[2], '-d', k])
            sys.stdout = sys.__stdout__
            expectedOutput = '\n'.join(v) + '\n'
            self.assertEqual(expectedOutput, capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()