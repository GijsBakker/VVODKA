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
import os

RUN = 1
SETTINGS = "Not Multi Processed Large Set"


def write_time(start_time, sequences_time, kmer_list_time, find_overlap_time, stop_time, cores, kmer, filenames):
    f = open("../Logs/log2.txt", "a")
    files = ", ".join([os.path.basename(os.path.normpath(file)) for file in filenames])

    f.write(f"\n{files}; cores: {cores}; kmer length: {kmer}\n")
    f.write(f"Start Time {start_time}\n")
    f.write(f"Time to get sequences {sequences_time - start_time}s.\n")
    f.write(f"Time to get kmers {kmer_list_time - sequences_time}s.\n")
    f.write(f"Time to get overlap {find_overlap_time - kmer_list_time}s.\n")
    f.write(f"Time to Plot {stop_time - find_overlap_time}s.\n")
    f.write(f"Stop Time {stop_time}\n")
    f.close()


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
    sequences = [ReadFasta.read_fasta(file) for file in files]

    sequences_time = time.time()

    kmer_list_time = None
    find_overlap_time = None

    # should compare all files
    indexes = [i for i in range(len(sequences))]
    while len(indexes) > 1:
        for i in indexes[1:len(indexes)]:
            first = indexes[0]
            print(f"Matching {files[first]} against {files[i]}")

            print("Finding overlapping sequences")
            # TODO: if given multiple files must compare each against each other
            positions, kmer_list_time, find_overlap_time = KMer.find_overlapping_kmers(sequences[first].seq, sequences[i].seq, kmer_size, cores)

            print("Making plot")
            CreateDotPlot.create_dot_plot(positions[0], positions[1], sequences[first], sequences[i])

        indexes = indexes[1:len(indexes)]

    stop_time = time.time()
    write_time(start_time, sequences_time, kmer_list_time, find_overlap_time, stop_time, cores, kmer_size, files)


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
