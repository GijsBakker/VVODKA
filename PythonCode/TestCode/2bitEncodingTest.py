#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts import TwoBitEncoding


class TestKmer(unittest.TestCase):
    def test_find_kmer(self):
        sequence = "ATCG"
        expected = bytearray(b'\x00\x03\x01\x02')
        got = TwoBitEncoding.string_to_two_bit(sequence)
        self.assertEqual(expected, got)

    def test_find_kmer_multiple_occurrences(self):
        sequence = "GGGG"
        expected = bytearray(b'\x02\x02\x02\x02')
        got = TwoBitEncoding.string_to_two_bit(sequence)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
