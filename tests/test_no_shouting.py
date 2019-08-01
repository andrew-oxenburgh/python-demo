# -*- coding: utf-8 -*-

from sample.no_shouting import no_shouting

import unittest

class NoShoutingTestSuite(unittest.TestCase):
    def test_1(self):
        """ when no capitals, return string as is"""
        self.assertEquals(no_shouting('1'), '1')
        self.assertEquals(no_shouting('a'), 'a')
        self.assertEquals(no_shouting('this is a long string'), 'this is a long string')

    def test_2(self):
        """ when capitals, convert them to lower case"""
        self.assertEquals(no_shouting('A'), 'a')
        self.assertEquals(no_shouting('this IS a long string'), 'this is a long string')
        self.assertEquals(no_shouting('HERE ARE LOTS OF CAPITALS'), 'here are lots of capitals')


if __name__ == '__main__':
    unittest.main()
