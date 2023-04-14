#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts.Old import KMer
from Scripts.TwoBitEncoding import string_to_two_bit


class TestKmer(unittest.TestCase):

    def test_find_kmer_compressed(self):
        kmer = bytearray(b'\x03\x03\x03')
        sequence = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                             b'\x00\x00\x00\x00\x00\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                             b'\x00\x03\x03\x03\x00\x00\x00\x00\x00')
        kmers_two = KMer.sequence_to_kmer(sequence, 3)
        expected = [27, 45]
        got = KMer.find_kmer(kmer, kmers_two)
        self.assertEqual(expected, got)

    def test_sequence_to_kmer(self):
        size = 3
        sequence = "ATCGT"
        expected = ["ATC", "GCT", "CGT"]
        got = KMer.sequence_to_kmer(sequence, size)
        self.assertEqual(expected, got)

    def test_sequence_to_kmer_small(self):
        size = 1
        sequence = "ATCGT"
        expected = ["A", "T", "C", "G", "T"]
        got = KMer.sequence_to_kmer(sequence, size)
        self.assertEqual(expected, got)

    def test_find_overlapping_kmers(self):
        size = 3
        #sequence = "ATCG"
        sequence = bytearray(b'\x03\x02\x01\x00')
        #sequence_two = "GATCG"
        sequence_two = bytearray(b'\x00\x03\x02\x01\x00')
        expected = [[0, 1], [1, 2]]
        got = KMer.find_overlapping_kmers(sequence, sequence_two, size, cores=8)
        self.assertEqual(expected, got)

    def test_find_multiple_overlapping_kmers(self):
        size = 3
        sequence = string_to_two_bit("ATCG")
        sequence_two = string_to_two_bit("GATCGATC")
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.find_overlapping_kmers(sequence, sequence_two, size, cores=8)
        self.assertEqual(expected, got)

    def test_find_group_kmers(self):
        kmers = KMer.sequence_to_kmer(string_to_two_bit("ATCGGG"), 3)
        kmer_two = KMer.sequence_to_kmer(string_to_two_bit("GATCGATC"), 3)
        expected = [[0,0,1],[1,5,2]]
        got = KMer.find_group_kmers(kmers, kmer_two, 0)
        self.assertEqual(expected, got)

    def test_find_group_kmers_mid_position(self):
        kmers = KMer.sequence_to_kmer(string_to_two_bit("ATCGGG"), 3)
        kmer_two = KMer.sequence_to_kmer(string_to_two_bit("GATCGATC"), 3)
        expected = [[100,100,101],[1,5,2]]
        got = KMer.find_group_kmers(kmers, kmer_two, 100)
        self.assertEqual(expected, got)

    def test_multi_process(self):
        kmers = KMer.sequence_to_kmer(string_to_two_bit("ATCG"), 3)
        kmer_two = KMer.sequence_to_kmer(string_to_two_bit("GATCGATC"), 3)
        threads = 4
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.multi_process(threads, kmers, kmer_two)
        self.assertEqual(expected, got)

    def test_multi_process_more_kmers(self):
        kmers = KMer.sequence_to_kmer(string_to_two_bit("ATCGGG"), 3)
        kmer_two = KMer.sequence_to_kmer(string_to_two_bit("GATCGATC"), 3)
        cores = 4
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.multi_process(cores, kmers, kmer_two)
        self.assertEqual(expected, got)

    def test_multi_process_match_in_last(self):
        kmers = KMer.sequence_to_kmer(string_to_two_bit("ATCGGGGAT"), 3)
        kmer_two = KMer.sequence_to_kmer(string_to_two_bit("GATCGATC"), 3)
        cores = 4
        expected = [[0, 0, 1, 6, 6], [1, 5, 2, 0, 4]]
        got = KMer.multi_process(cores, kmers, kmer_two)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
