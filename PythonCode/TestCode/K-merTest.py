#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts import KMer
from Scripts.TwoBitEncoding import string_to_two_bit


class TestKmer(unittest.TestCase):

     # def test_find_kmer(self):
     #    kmer = bytearray(b'\x03\x02\x01\x00')
     #    sequence = bytearray(b'\x03\x02\x01\x00\x00\x00\x02\x03\x02\x01')
     #    expected = [0, 7]
     #    got = KMer.find_kmer(kmer, sequence)
     #    self.assertEqual(expected, got)

    def test_find_kmer_compressed(self):
        kmer = bytearray(b'\x03\x03\x03')
        sequence = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                             b'\x00\x00\x00\x00\x00\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                             b'\x00\x03\x03\x03\x00\x00\x00\x00\x00')
        expected = [27, 45]
        got = KMer.find_kmer(kmer, sequence)
        self.assertEqual(expected, got)

    def test_sequence_to_kmer(self):
        size = 3
        sequence = "ATCGT"
        expected = ["ATC", "TCG", "CGT"]
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
        got, time_one, time_two = KMer.find_overlapping_kmers(sequence, sequence_two, size, cores=8)
        self.assertEqual(expected, got)

    def test_find_multiple_overlapping_kmers(self):
        size = 3
        sequence = string_to_two_bit("ATCG")
        sequence_two = string_to_two_bit("GATCGATC")
        expected = [[0, 0, 1], [1, 5, 2]]
        got, time_one, time_two = KMer.find_overlapping_kmers(sequence, sequence_two, size, cores=8)
        self.assertEqual(expected, got)

    def test_find_group_kmers(self):
        kmers = [string_to_two_bit(x) for x in ["ATC", "TCG", "CGG", "GGG"]]
        sequence = string_to_two_bit("GATCGATC")
        expected = [[0,0,1],[1,5,2]]
        got = KMer.find_group_kmers(kmers, sequence, 0)
        self.assertEqual(expected, got)

    def test_find_group_kmers_mid_position(self):
        kmers = [string_to_two_bit(x) for x in ["ATC", "TCG", "CGG", "GGG"]]
        sequence = string_to_two_bit("GATCGATC")
        expected = [[100,100,101],[1,5,2]]
        got = KMer.find_group_kmers(kmers, sequence, 100)
        self.assertEqual(expected, got)

    def test_multi_process(self):
        kmers = [string_to_two_bit(x) for x in ["ATC", "TCG"]]
        sequence = string_to_two_bit("GATCGATC")
        threads = 4
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.multi_process(threads, kmers, sequence)
        self.assertEqual(expected, got)

    def test_multi_process_more_kmers(self):
        kmers = [string_to_two_bit(x) for x in ["ATC", "TCG", "CGG", "GGG"]]
        sequence = string_to_two_bit("GATCGATC")
        cores = 4
        expected = [[0, 0, 1], [1, 5, 2]]
        got = KMer.multi_process(cores, kmers, sequence)
        self.assertEqual(expected, got)

    def test_multi_process_match_in_last(self):
        kmers = [string_to_two_bit(x) for x in ["ATC", "TCG", "CGG", "GGG", "GGG", "GGA", "GAT"]]
        sequence = string_to_two_bit("GATCGATC")
        cores = 4
        expected = [[0, 0, 1, 6, 6], [1, 5, 2, 0, 4]]
        got = KMer.multi_process(cores, kmers, sequence)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
