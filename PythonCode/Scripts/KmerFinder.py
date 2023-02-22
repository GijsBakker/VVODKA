#!/usr/bin/python3

"""
KMer.py: Is used to find k-mers in genomes
"""

import re
import threading


class KmerFinder:
    x = -1
    pos_y = []
    pos_x = []

    def __init__(self, pos_x, k_mer, sequence):
        self.x = pos_x
        thread = threading.Thread(target=self.find_kmer, args=(k_mer, sequence))
        thread.start()
        # self.find_kmer(k_mer, sequence)

    def find_kmer(self, k_mer, sequence):
        """
        This function compare looks for a k-mer within a sequence
        :parallel: This function can be run next to other functions with different k_mers
        :param k_mer: a k_mer string
        :param sequence: a sequence string
        :return: a list of the positions of the found kmers
        """
        self.pos_y = [match.start() for match in re.finditer(k_mer, sequence)]
        self.pos_x = [self.x for i in range(len(self.pos_y))]


"""
    # multi threaded way of 
    kmers = []
    percentage = 0
    for position_x, kmer in enumerate(kmer_list):
        #if position_x / len(kmer_list) >= percentage:
         #   print(position_x / len(kmer_list) * 100, "%")
          #  percentage += 0.001

        kmers.append(KmerFinder(position_x, str(kmer), str(sequence_two)))

    print("combining positions")
    for kmer in kmers:
        positions_x += kmer.pos_x
        positions_y += kmer.pos_y"""