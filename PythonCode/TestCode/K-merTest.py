#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
# unit test case
import unittest
from Scripts import KMer


class TestKmer(unittest.TestCase):
    # test function to test equality of two value
    def test_kmer(self):
        kmer = "ATC"
        sequence = "ATCGGGTATC"
        expected = [0, 7]
        got = KMer.find_kmer(kmer, sequence)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
