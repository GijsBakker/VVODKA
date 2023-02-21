#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""


def find_kmer(k_mer, sequence):
    """
    This function compare looks for a k-mer within a sequence
    :parallel: This function can be run next to other functions with different k_mers
    :param k_mer: a k_mer string
    :param sequence: a sequence string
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


def sequence_to_kmer(sequence, kmer_size):
    """
    This function splits a sequence into k_mers
    :parallel: This function is necessary for a parallel program. This function wil be run so after each thread can have
    its own k_mers. This function is not necessary when not run in parallel.
    :param sequence: A string of the sequence
    :param kmer_size: The size of the k_mers. Has to be more than 0 and not larger than the sequence
    :return: A list of all the K_mers
    """
    kmers = []
    for start in range(len(sequence)-kmer_size+1):
        kmers.append(sequence[start:start+kmer_size])
    return kmers
