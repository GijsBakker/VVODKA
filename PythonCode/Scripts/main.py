#!/usr/bin/python3

"""
Main.py: main.py is used to handle the user input, call the right functions and return the final output
"""

__author__ = "Gijs Bakker"
__version__ = 0.1

import CreateDotPlot
import KMer
import ReadFasta


TESTSEQONE = "ATCG"
TESTSEQTWO = "GATCGATC"


def main():
    sequenceOne = ReadFasta.read_fasta("../data/prochlorococcus/LG.fa")
    sequenceOne = ReadFasta.read_fasta("../data/prochlorococcus/MED4.fa")
    size = 3
    positions = KMer.find_overlapping_kmers(sequence_one, sequence_two, size)
    CreateDotPlot.create_dot_plot(positions[0], positions[1], sequence_one, sequence_two)


if __name__ == '__main__':
    main()
