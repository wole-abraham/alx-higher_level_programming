#!/usr/bin/python3

""" Python test module """

import unittest

res = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max_integer """

    def test_max(self):

        """ Test for max value """

        self.assertAlmostEqual(res([1, 4, 6]), 6)
        self.assertIsNone(res([]))
