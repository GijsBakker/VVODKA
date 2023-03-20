#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts import KMer
from Scripts.TwoBitEncoding import string_to_two_bit


class TestKmer(unittest.TestCase):
    def test_sequence_to_kmer_dict(self):
        size = 3
        sequence = "ATCG"
        expected = {'ATC': [0],
                    'TCG': [1]}
        got = KMer.sequence_to_kmer_dict(sequence, size)
        self.assertEqual(expected, got)

    def test_sequence_to_kmer_dict_multiple(self):
        size = 3
        sequence = "ATCGCGC"
        expected = {'ATC': [0],
                    'TCG': [1],
                    'CGC': [2,4],
                    'GCG': [3]}
        got = KMer.sequence_to_kmer_dict(sequence, size)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()