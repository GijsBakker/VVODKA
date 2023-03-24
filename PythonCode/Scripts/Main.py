#!/usr/bin/python3
import pyfastx

usage = """
Main.py: Main.py is used to handle the user input, call the right functions and return the final output

Usage:
Main.py -k <kmerSize> -c <cores> [-s] (-f <file>) ... [-m <merged_file>] ...
Main.py (-h | --help | --version)
"""

__author__ = "Gijs Bakker"
__version__ = 0.1

from docopt import docopt
import InlineKmer
import FastaSequence
import CreateDotPlot
import KMer
import ReadFasta
import time
import os

RUN = 1
SETTINGS = "Testing inline"
FILE = "../Logs/log3.txt"


def write_time(start_time, stop_time, cores, kmer, filenames):
    f = open(FILE, "a")
    files = ", ".join([os.path.basename(os.path.normpath(file)) for file in filenames])

    f.write(f"\n{SETTINGS}; cores: {cores}; kmer length: {kmer}\n")
    f.write(f"files: {files}\n")
    f.write(f"Time {stop_time - start_time}\n")
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
    on_self = args['-s']
    merged_files = args['<merged_file>']

    print("Extracting Sequences")
    # TODO Can be its own function until sequences is filled
    sequences = []
    for file in files:
        to_be_combined = []
        for seq in ReadFasta.read_fasta(file):
            to_be_combined.append(seq)
        if file in merged_files:
            # should combine each of the to be combined into one pyfastx.Sequence
            sequences.append(FastaSequence.FastaSequence(file,
                                                         "".join([x.seq for x in to_be_combined])))
        else:
            sequences += [FastaSequence.FastaSequence(x.name, x.seq) for x in to_be_combined]

    # if sequences is one and on self is not given there are no plots to be made
    if not on_self and len(sequences) <= 1:
        print("Only one file with one sequence given. Auto plotted on itself")
        on_self = True

    # should compare all files
    indexes = [i for i in range(len(sequences))]

    # TODO can be its own function until the positions are filled
    # check if plot against self should be made
    if on_self:
        start = 0
    else:
        start = 1

    positions = []

    # find all overlapping k-mers
    while len(indexes) > start:
        for i in indexes[start:len(indexes)]:
            first = indexes[0]
            print(f"Matching {sequences[first].name} against {sequences[i].name}")

            print("Finding overlapping sequences")
            # positions.append(KMer.find_overlapping_kmers(sequences[first].seq, sequences[i].seq, kmer_size, cores)
            #                  + [sequences[first].name, sequences[i].name])
            positions.append(InlineKmer.find_overlapping_kmers(sequences[first].seq, sequences[i].seq, kmer_size)
                             + [sequences[first].name, sequences[i].name])

        indexes = indexes[1:len(indexes)]

    # create plots
    print("Making plots")

    for position in positions:
        fig, file = CreateDotPlot.create_dot_plot(position[0], position[1], position[2], position[3], kmer_size)
        fig.savefig(file, dpi=300)

    stop_time = time.time()
    write_time(start_time, stop_time, cores, kmer_size, files)


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
