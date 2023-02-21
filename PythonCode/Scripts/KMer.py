#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""


def find_kmer(k_mer, sequence):
    """
    This function compare looks for a k-mer within a sequence
    :return: a list of the positions of the found kmers
    """
    # TODO determine where the position is marked. (The first of the kmer or in the middle. Even number can be a
    #  problem)
    kmer_len = len(k_mer)
    positions = []
    for pos in range(len(sequence)):
        if sequence[pos:pos+kmer_len] == k_mer:
            positions.append(pos)
    return positions
