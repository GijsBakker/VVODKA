#!/usr/bin/python3

usage = """
"""

__author__ = "Gijs Bakker"
__version__ = 0.1


def find_all(sub, a_str):
    """
    This function finds all occurrences of a sub string in another string
    :param sub: a substring
    :param a_str: a string on which the substring needs to be found
    :return: The coordinates of the substring within the complete string
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)   # use start += 1 to find overlapping matches


def invert_kmer(kmer):
    """
    This function takes a two bit representation of a k-mer and inverts set k-mer
    :param kmer: a two bit representation of a k-mer
    :return: the inversion of the given kmer
    """

    invert_dict = {
        3: 0b00,
        0: 0b11,
        1: 0b10,
        2: 0b01
    }
    inverted_kmer = bytearray('', encoding='utf-8')
    for byte in kmer:
        inverted_kmer.append(invert_dict[byte])

    return inverted_kmer


def find_overlap_kmers(seq1, seq2, kmer_length, wanted_length, max_misses):
    """
    This function finds all positions where k-mers overlap between two dna sequences.
    :param seq1: String of sequence one
    :param seq2: String of sequence two
    :param kmer_length:
    :param wanted_length:
    :param max_misses:
    :return:
    """
    # TODO object instead of list
    # TODO shorten code if possible
    possible_kmers = []
    final_kmers = []

    for x_pos in range(len(seq1) - kmer_length + 1):
        kmer = seq1[x_pos:x_pos + kmer_length]
        kmer_rev = invert_kmer(kmer[::-1])
        y_kmers = []
        x_kmers = []
        if kmer in seq2:
            y_kmers += [y_pos for y_pos in find_all(kmer, seq2)]
            x_kmers += [x_pos for y_pos in range(len(y_kmers))]
        if kmer_rev in seq2 and kmer != kmer_rev:
            y_kmers += [y_pos for y_pos in find_all(kmer_rev, seq2)]
            x_kmers += [x_pos for y_pos in range(len(y_kmers))]

        new_kmers = list(zip(x_kmers, y_kmers))
        to_be_deleted = []
        # Check per existing kmer if a newfound kmer fits on it
        for kmer in possible_kmers:
            if not kmer[1] in new_kmers:     # if not found add one miss
                kmer[2] += 1    # +1 misses

            kmer[1] = (kmer[1][0] + 1, kmer[1][1] + kmer[4])  # update next wanted kmer.
            kmer[3] += 1  # +1 len

            if kmer[2] > max_misses:
                to_be_deleted.append(kmer)
            elif kmer[3] >= wanted_length:
                final_kmers.append(kmer[0])
                to_be_deleted.append(kmer)

        # remove to be deleted kmers
        for kmer in to_be_deleted:
            possible_kmers.remove(kmer)

        # Add new kmer up and down
        for kmer in new_kmers:
            possible_kmers.append([kmer, (kmer[0]+1, kmer[1]+1), 0, 1, 1])
            possible_kmers.append([kmer, (kmer[0]+1, kmer[1]-1), 0, 1, -1])

    return final_kmers


def unzip_kmers(kmer_list):
    return list(zip(*kmer_list))


def find_overlapping_kmers(seq1, seq2, kmer_length, wanted_length, max_misses):
    print("loop")
    print(len(seq1), len(seq2))
    zipped = find_overlap_kmers(seq1, seq2, kmer_length, wanted_length, max_misses)
    print(len(zipped))
    unzipped = unzip_kmers(zipped)
    return [list(unzipped[0]), list(unzipped[1])]
