#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
# unit test case
import unittest
from Scripts import KMer


class TestKmer(unittest.TestCase):
    # test function to test equality of two value
    def test_find_kmer(self):
        kmer = "ATC"
        sequence = "ATCGGGTATC"
        expected = [0, 7]
        got = KMer.find_kmer(kmer, sequence)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)

    def test_sequence_to_kmer(self):
        size = 3
        sequence = "ATCGT"
        expected = ["ATC", "TCG", "CGT"]
        got = KMer.sequence_to_kmer(sequence, size)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)

    def test_sequence_to_kmer_small(self):
        size = 1
        sequence = "ATCGT"
        expected = ["A", "T", "C", "G", "T"]
        got = KMer.sequence_to_kmer(sequence, size)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)

    def test_find_overlapping_kmers(self):
        size = 3
        sequence = "ATCG"
        sequence_two = "GATCG"
        expected = [[0, 1], [1, 2]]
        got = KMer.find_overlapping_kmers(sequence, sequence_two, size)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)

    def test_find_multiple_overlapping_kmers(self):
        size = 3
        sequence = "ATCG"
        sequence_two = "GATCGATC"
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.find_overlapping_kmers(sequence, sequence_two, size)
        # assertEqual() to check equality of first & second value
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
