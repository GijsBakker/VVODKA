#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts.Old import KMer


class TestKmer(unittest.TestCase):
    def test_kmers_to_sequence(self):
        x = [1,2,3,4,5,6]
        y = [10,11,12,13,14,15]
        got = KMer.kmers_in_sequence(x, y, 6, 0)
        expected = [[1], [10]]
        self.assertEqual(expected, got)

    def test_kmers_to_sequence_interrupted(self):
        x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        y = [10, 20, 11, 23, 12, 1, 13, 90, 14, 100, 15, 32]
        got = KMer.kmers_in_sequence(x, y, 6, 0)
        expected = [[1], [10]]
        self.assertEqual(expected, got)

    def test_kmers_to_sequence_two_nested_sequences(self):
        x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        y = [10, 20, 11, 21, 12, 22, 13, 23, 14, 24, 15, 25]
        got = KMer.kmers_in_sequence(x, y, 6, 0)
        expected = [[1, 1], [10, 20]]
        self.assertEqual(expected, got)

    def test_kmers_to_sequence_decreasing(self):
        x = [1, 2, 3, 4, 5, 6]
        y = [6, 5, 4, 3, 2, 1]
        got = KMer.kmers_in_sequence(x, y, 6, 0)
        expected = [[1], [6]]
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
