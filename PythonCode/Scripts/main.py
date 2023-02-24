#!/usr/bin/python3

usage = """
Main.py: main.py is used to handle the user input, call the right functions and return the final output

Usage:
main.py -k <kmerSize> -c <cores> -f <file> <file> ... 
main.py (-h | --help | --version)
"""

__author__ = "Gijs Bakker"
__version__ = 0.1

from docopt import docopt
import CreateDotPlot
import KMer
import ReadFasta
import time

RUN = 1
SETTINGS = "Not Multi Processed Large Set"


def main(args):
    """
    This validates all given arguments
    :param args: docopt arguments
    """
    start_time = time.time()
    kmer_size = int(args['<kmerSize>'])
    files = args['<file>']
    cores = int(args['<cores>'])

    print("Extracting Sequences")
    sequences = [ReadFasta.read_fasta(file).seq for file in files]

    print("Finding overlapping sequences")
    # TODO: if given multiple files must compare each against each other
    positions = KMer.find_overlapping_kmers(sequences[0], sequences[1], kmer_size, cores)

    print("Making plot")
    CreateDotPlot.create_dot_plot(positions[0], positions[1], sequences[0], sequences[1])

    stop_time = time.time()
    # f = open("../Logs/log.txt", "a")
    # f.write(f"Run {RUN} with settings {SETTINGS}: time {stop_time - start_time} seconds\n")
    # f.close()


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
