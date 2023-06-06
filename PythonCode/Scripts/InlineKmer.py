#!/usr/bin/python3


__author__ = "Gijs Bakker"
__version__ = 0.1


def find_all(sub, genome):
    """
    This function finds all occurrences of a sub string in another string
    :param sub: a substring
    :param genome: a string of the genome in which the substring needs to be found
    :return: The coordinates of the substring within the complete string
    """
    start = 0
    while True:
        start = genome.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1


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


def find_overlap_kmers(seq1, seq2, kmer_length):
    """
    This function finds all positions where k-mers overlap between two dna sequences.
    :param seq1: String of sequence one
    :param seq2: String of sequence two
    :param kmer_length: The length of the k-mers
    :return: A list containing lists of x and y coordinates
    """
    final_kmers = []

    for x_pos in range(len(seq1) - kmer_length +1):
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

        final_kmers += list(zip(x_kmers, y_kmers))
    return final_kmers


def unzip_kmers(kmer_list):
    return list(zip(*kmer_list))


def find_overlapping_kmers(seq1, seq2, kmer_length):
    zipped = find_overlap_kmers(seq1, seq2, kmer_length)
    unzipped = unzip_kmers(zipped)

    # if none overlapping kmers are found
    if len(unzipped) < 1:
        unzipped = [[], []]

    return [list(unzipped[0]), list(unzipped[1])]
