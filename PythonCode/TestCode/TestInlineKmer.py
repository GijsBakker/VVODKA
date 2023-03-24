#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts import InlineKmer
from Scripts.TwoBitEncoding import string_to_two_bit


class TestKmer(unittest.TestCase):
    def test_find_overlap_kmers(self):
        sequence_one = string_to_two_bit("TTT")
        sequence_two = string_to_two_bit("AAAAATTTAAAAAAATTTAA")
        got = InlineKmer.find_overlap_kmers(sequence_one, sequence_two, 3)
        expected = [(0, 5), (0, 15)]
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
