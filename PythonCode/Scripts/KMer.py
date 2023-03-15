#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""
import math
import re
import time

import multiprocessing as mp


def find_kmer(k_mer, sequence):
    """
    This function compare looks for a k-mer within a sequence
    :param k_mer: bytearray representing the k-mer
    :param sequence: bytearray representing the sequence
    :return: a list of the positions of the found kmers
    """
    pattern = re.compile(bytes(k_mer))
    # return [match.start() for match in re.finditer(k_mer, sequence)]
    return [match.start() for match in pattern.finditer(sequence)]


def sequence_to_kmer(sequence, kmer_size):
    """
    This function splits a sequence into k_mers
    :param sequence: A string of the sequence
    :param kmer_size: The size of the k_mers. Has to be more than 0 and not larger than the sequence
    :return: A list of all the K_mers
    """
    kmers = []
    for start in range(len(sequence)-kmer_size+1):
        kmers.append(sequence[start:start+kmer_size])
    return kmers


def find_group_kmers(kmers, sequence, start_pos_x):
    """
    This function takes a group of kmers and find all those kmers in the given sequence
    :param start_pos_x: The position of these kmers within the first sequence
    :param kmers: List of bytearrays representing the k-mer
    :param sequence: bytearray representing the sequence
    :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
    """
    pos_y = []
    pos_x = []

    for kmer_number, kmer in enumerate(kmers):
        kmers = find_kmer(kmer, sequence)
        pos_y += kmers
        pos_x += [start_pos_x + kmer_number for i in range(len(kmers))]

    return [pos_x, pos_y]


def multi_run_wrapper(args):
    """
    This function is a way to have multiple arguments in one multiprocess call
    :param args: The arguments from a multiprocess function call
    :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
    """
    return find_group_kmers(*args)


def multi_process(cores, kmers, sequence):
    """
    This function finds given kmers in a sequence. It does this in a way that supports using multiple cores.
    :param cores: number of cores
    :param kmers: A list of bytearrays representing the k-mer
    :param sequence: bytearray representing the sequence
    :return: The found positions within a list: [[x1,x2,...], [y1,y2,...]]
    """
    # split kmers in equal groups
    kmer_range = math.floor(len(kmers)/cores)
    kmer_groups = []
    if kmer_range >= 1:
        for i in range(cores-1):
            kmer_groups.append([kmer for kmer in kmers[i*kmer_range: (i+1)*kmer_range]])

    # add last group which is smaller
    kmer_groups.append(kmers[(cores-1)*kmer_range: len(kmers)])

    pos_x = []
    pos_y = []

    # multi Processed
    p = mp.Pool(processes=cores)
    args = [[kmer_group, sequence, start_pos_x*kmer_range] for start_pos_x, kmer_group in enumerate(kmer_groups)]
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

    print("Searching for matches")

    positions_x, positions_y = multi_process(cores, kmer_list, sequence_two)
    overlap_positions = [positions_x, positions_y]
    return overlap_positions
