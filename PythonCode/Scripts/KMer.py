#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""

__author__ = "Gijs Bakker"
__version__ = 0.1


import math
import re
import time

import multiprocessing as mp


def kmers_in_sequence(x_positions, y_positions, number=5, margin=1):
    """
    This function removes all found kmers that are not a sequence of *number kmers. They can have *margin gaps
    :param x_positions: A list of x positions of the found kmers. First element of Y should point to first element of X
    :param y_positions: A list of y positions of the found kmers. First element of X should point to first element of Y
    :param number: The number of kmers that need to be in sequence for it not to be removed
    :param margin: The amount of gaps allowed in this sequence of kmers
    :return: A list of a list of x positions and a list of y positions
    """
    # TODO Right now only allows sequences with gaps. A shift upwards halfway is not recognized. (insertions or
    #  deletions are not recognized, only punt mutations)
    # TODO add this functionality in line
    # TODO Maybe recursive

    y_sequence = []
    x_sequence = []

    # loop over all x_positions
    for index, x in enumerate(x_positions):
        current_y = y_positions[index]
        misses = 0

        for i in range(number-1):     # should check if x+i exist for range given number
            i += 1
            if misses > margin:
                break   # Exceeded margin no need to check further

            amount = x_positions.count(x+i)
            if amount:       # check if x[x+i] exists
                # should get corresponding y
                # index only returns first index, should check all
                count = 0
                found = False
                current_index = 0
                while count < amount:
                    current_index = x_positions.index(x+i, current_index+1)
                    next_y = y_positions[current_index]
                    count += 1
                    # should check if y = one bigger or smaller than the previous y.
                    if next_y == current_y+1 or next_y == current_y - 1:
                        current_y = next_y
                        found = True

                if not found:
                    misses += 1
            else:
                misses += 1    # should mark an error

        if misses <= margin:
            x_sequence.append(x)    # can mark this kmer
            y_sequence.append(y_positions[index])

    return [x_sequence, y_sequence]


def find_kmer(k_mer, kmers_two):
    """
    This function compare looks for a k-mer within a sequence
    :param k_mer: bytearray representing the k-mer
    :param kmers_two: bytearray representing the sequence
    :return: a list of the positions of the found kmers
    """
    return [idx for idx, value in enumerate(kmers_two) if value == k_mer]


def sequence_to_kmer(sequence, kmer_size):
    """
    This function splits a sequence into k_mers
    :param sequence: A string of the sequence
    :param kmer_size: The size of the k_mers. Has to be more than 0 and not larger than the sequence
    :return: A list of all the K_mers
    """
    kmers = []
    for start in range(len(sequence)-kmer_size+1):
        kmer = sequence[start:start+kmer_size]
        # check if reversed is alphabetically lower
        kmers.append(min(kmer, kmer[::-1]))
    return kmers


def find_group_kmers(kmers_one, kmers_two, start_pos_x):
    """
    This function takes a group of kmers and find all those kmers in the given sequence
    :param start_pos_x: The position of these kmers within the first sequence
    :param kmers_one: List of bytearrays representing the k-mer
    :param kmers_two: bytearray representing the sequence
    :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
    """
    pos_y = []
    pos_x = []

    for kmer_number, kmer in enumerate(kmers_one):
        found_kmers = find_kmer(kmer, kmers_two)
        pos_y += found_kmers
        pos_x += [start_pos_x + kmer_number for i in range(len(found_kmers))]

    return [pos_x, pos_y]


def multi_run_wrapper(args):
    """
    This function is a way to have multiple arguments in one multiprocess call
    :param args: The arguments from a multiprocess function call
    :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
    """
    return find_group_kmers(*args)


def multi_process(cores, kmers_one, kmers_two):
    """
    This function finds given kmers in a sequence. It does this in a way that supports using multiple cores.
    :param cores: number of cores
    :param kmers_one: A list of bytearrays representing the k-mer
    :param kmers_two: bytearray representing the sequence
    :return: The found positions within a list: [[x1,x2,...], [y1,y2,...]]
    """
    # split kmers in equal groups
    kmer_range = math.floor(len(kmers_one) / cores)
    kmer_groups = []
    if kmer_range >= 1:
        for i in range(cores-1):
            kmer_groups.append([kmer for kmer in kmers_one[i * kmer_range: (i + 1) * kmer_range]])

    # add last group which is smaller
    kmer_groups.append(kmers_one[(cores - 1) * kmer_range: len(kmers_one)])

    pos_x = []
    pos_y = []

    # multi Processed
    p = mp.Pool(processes=cores)
    args = [[kmer_group, kmers_two, start_pos_x * kmer_range] for start_pos_x, kmer_group in enumerate(kmer_groups)]
    all_data = p.map(multi_run_wrapper, args)

    # unpack data for each run
    for data in all_data:
        pos_x += data[0]
        pos_y += data[1]

    return [pos_x, pos_y]


def find_overlapping_kmers(sequence_one, sequence_two, size, cores):
    """
    This function finds the overlapping kmers between two sequences.
    :param sequence_one: bytearray of the first sequence
    :param sequence_two: bytearray of the second sequence
    :param size: size of the kmers. Cannot be smaller than 1
    :return: The found positions within a list: [[x1,x2,...], [y1,y2,...]]
    """
    print("Getting K-mers")
    kmer_list = sequence_to_kmer(sequence_one, size)
    kmer_list_two = sequence_to_kmer(sequence_two, size)

    print("Searching for matches")
    positions_x, positions_y = multi_process(cores, kmer_list, kmer_list_two)
    print("Finding in sequence")
    positions_x, positions_y = kmers_in_sequence(positions_x, positions_y)
    overlap_positions = [positions_x, positions_y]
    return overlap_positions
