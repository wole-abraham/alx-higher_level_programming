#!/usr/bin/python3

""" Python test module """

import unittest

res = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max_integer """

    def test_max(self):

        """ Test for max value """

        self.assertAlmostEqual(res([1, 4, 6]), 6)
        self.assertAlmostEqual(res([5, 3, 4]), 5)
        self.assertAlmostEqual(res([3, 5, 2]), 5)
        self.assertAlmostEqual(res([-1, 3, 5]), 5)
        self.assertAlmostEqual(res([-1, -4, -10]), -1)
        self.assertAlmostEqual(res([2]), 2)
        self.assertIsNone(res([]))
