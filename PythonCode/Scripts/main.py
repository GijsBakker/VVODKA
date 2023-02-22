#!/usr/bin/python3

usage = """
GenomeDotPlotter

Usage:
main.py -k <kmerSize> -f <file> <file> ...
main.py (-h | --help | --version)
"""

"""
Main.py: main.py is used to handle the user input, call the right functions and return the final output
"""


__author__ = "Gijs Bakker"
__version__ = 0.1

import CreateDotPlot
import KMer
import ReadFasta
from docopt import docopt


def main(args):
    """
    This validates all given arguments
    :param args: docopt arguments
    """
    kmer_size = int(args['<kmerSize>'])
    files = args['<file>']

    print("Extracting Sequences")
    sequences = [ReadFasta.read_fasta(file).seq for file in files]

    print("Finding overlapping sequences")
    # TODO: if given multiple files must compare each against each other
    positions = KMer.find_overlapping_kmers(sequences[0], sequences[1], kmer_size)

    print("Making plot")
    CreateDotPlot.create_dot_plot(positions[0], positions[1], sequences[0], sequences[1])


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
