#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""

import re


def find_kmer(k_mer, sequence):
    """
    This function compare looks for a k-mer within a sequence
    :parallel: This function can be run next to other functions with different k_mers
    :param k_mer: a k_mer string
    :param sequence: a sequence string
    :return: a list of the positions of the found kmers
    """
    return [match.start() for match in re.finditer(k_mer, sequence)]


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


def find_overlapping_kmers(sequence_one, sequence_two, size):
    """
    This function finds the overlapping kmers between two sequences.
    :parallel: In parallel the biggest sequence needs to be split into kmers. This wil increase speed.
        The kmers can be split over multiple processes.
    :param sequence_one: string of the first sequence
    :param sequence_two: string of the second sequence
    :param size: size of the kmers. Cannot be smaller than 1
    :return:
    """
    print("Getting K-mers")
    kmer_list = sequence_to_kmer(sequence_one, size)
    positions_x = []
    positions_y = []

    print("Searching for matches")
    percentage = 0
    for position_x, kmer in enumerate(kmer_list):

        kmers = find_kmer(str(kmer), str(sequence_two))
        positions_y += kmers
        positions_x += [position_x for i in range(len(kmers))]
    overlap_positions = [positions_x, positions_y]
    return overlap_positions

