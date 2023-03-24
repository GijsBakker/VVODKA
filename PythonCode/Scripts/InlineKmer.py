import re


def find_all(sub, a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)   # use start += 1 to find overlapping matches


def find_overlap_kmers(seq1, seq2, kmer_length):
    kmer_list = []
    for x_pos in range(len(seq1) - kmer_length + 1):
        kmer = seq1[x_pos:x_pos + kmer_length]
        kmer_rev = kmer[::-1]
        if kmer in seq2:
            y_kmers = [y_pos for y_pos in find_all(kmer, seq2)]
            x_kmers = [x_pos for y_pos in range(len(y_kmers))]
            kmer_list += list(zip(x_kmers, y_kmers))
        if kmer_rev in seq2 and kmer != kmer_rev:
            y_kmers = [y_pos for y_pos in find_all(kmer_rev, seq2)]
            x_kmers = [x_pos for y_pos in range(len(y_kmers))]
            kmer_list += list(zip(x_kmers, y_kmers))
    return kmer_list


def unzip_kmers(kmer_list):
    return list(zip(*kmer_list))


def find_overlapping_kmers(seq1, seq2, kmer_length):
    zipped = find_overlap_kmers(seq1, seq2, kmer_length)
    unzipped = unzip_kmers(zipped)
    return [list(unzipped[0]), list(unzipped[1])]
