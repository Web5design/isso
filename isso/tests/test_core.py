# -*- encoding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import io

from isso import core


class TestConfig(unittest.TestCase):

    def test_parser(self):

        parser = core.IssoParser(allow_no_value=True)
        parser.read_file(io.StringIO(u"""
            [foo]
            bar = 1h
            baz = 12
            spam = a, b, cdef
            bla =
                spam
                ham
            asd = fgh"""))

        self.assertEqual(parser.getint("foo", "bar"), 3600)
        self.assertEqual(parser.getint("foo", "baz"), 12)
        self.assertEqual(parser.getlist("foo", "spam"), ['a', 'b', 'cdef'])
        self.assertEqual(list(parser.getiter("foo", "bla")), ['spam', 'ham'])
        self.assertEqual(list(parser.getiter("foo", "asd")), ['fgh'])
