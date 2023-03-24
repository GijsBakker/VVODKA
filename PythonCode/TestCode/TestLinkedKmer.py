#!/usr/bin/python3

"""
K-merTest: is used to test the functions in the KMer script
"""
import unittest
from Scripts.LinkedKmer import LinkedKmer


class TestKmer(unittest.TestCase):
    def test_LinkedKmer(self):
        linked_kmer = LinkedKmer(1, 1, True, False)
        linked_two = LinkedKmer(1, 2, True, False)
        linked_kmer.set_next(linked_two)
        got = next(linked_kmer)
        self.assertEqual(linked_two, got)

    def test_LinkedKmer_iter(self):
        linked_kmer = LinkedKmer(1, 1, True, False)
        linked_two = LinkedKmer(2, 2, True, False)
        linked_three = LinkedKmer(3, 3, True, False)
        linked_kmer.set_next(linked_two)
        linked_two.set_next(linked_three)


if __name__ == '__main__':
    unittest.main()
