#!/usr/bin/python3

usage = """
VVODKA.py: VVODKA.py is used to handle the user input, call the right functions and return the final output

Usage:
    VVODKA.py -k <kmer_size> [-r <dpi>] [-s <self>] [-d <dot_size>] <files>...
    VVODKA.py (-h | --help | --version)
    
Options:
    -k <kmer_size>  Specify the size of the k-mer
    -r <dpi>        Specify the DPI [default: 600]
    -s <self>       Specify if files should be plotted against themselves, use Y to plot against itself or N to not 
                    plot against itself [default: Y]
    -d <dot_size>   Specify the dot size to be used in the dot plot [default: 2]
    <files>...      Specify the files which are plotted against each other
"""

__author__ = "Gijs Bakker"
__version__ = 1.0

from docopt import docopt
import InlineKmer
import FastaSequence
import CreateDotPlot
import ReadFasta
import time
from Logger import logger


def get_sequences(files):
    """
    This function extract the sequences and name from a list of fasta files
    :param files: a list of fasta files
    :return: a list containing FastaSequence objects
    """
    sequences = []
    for file in files:
        to_be_combined = []
        for seq in ReadFasta.read_fasta(file):
            to_be_combined.append(seq)
        else:
            sequences += [FastaSequence.FastaSequence(x.name, x.seq) for x in to_be_combined]
    return sequences


def get_plot_info(on_self, sequences, kmer_size):
    """
    This function finds the locations of overlapping k-mers when given sequences.
    :param on_self: Boolean indicating if sequences should be plotted on themselves
    :param sequences: A list containing all sequences
    :param kmer_size: A integer giving the wanted k-mer size
    :return: A list containing lists of the x and y coordinates of the overlapping k-mers, the used k-mer size and the
    names of the sequences compared.
    """
    plot_info_list = []

    # check if plot against self should be made
    if on_self:
        start = 0
    else:
        start = 1

    # should compare all files
    indexes = [i for i in range(len(sequences))]

    # find all overlapping k-mers
    while len(indexes) > start:
        for i in indexes[start:len(indexes)]:
            first = indexes[0]

            print(f"Matching {sequences[first].name} against {sequences[i].name}")
            if sequences[first].name == sequences[i].name:
                names = [sequences[first].name, ""]
            else:
                names = [sequences[first].name, sequences[i].name]

            print("Finding overlapping sequences")
            plot_info_list.append(InlineKmer.find_overlapping_kmers(sequences[first].seq, sequences[i].seq, kmer_size)
                                  + names)

        indexes = indexes[1:len(indexes)]
    return plot_info_list


def vvodka(kmer_size, files, on_self, dpi, dot_size):
    """
    This function creates genome dot plots corresponding to the input data.
    :param kmer_size: The wanted k-mer size used to find overlapping k-mers
    :param files: A list of fasta files, used to create the genome dot plots.
    :param on_self: String that marks if genomes should be plotted on itself.
    :param dpi: The resolution of the plot
    :param dot_size: The size of the dots
    """

    # Check if arguments are correctly specified
    if on_self.upper() not in ['Y', 'N']:
        print("Please set -s to either Y or N")
        return
    if on_self.upper() == 'N' and len(files) <= 1:
        print("No plots to make, make sure that you specify multiple files when using -s=N")
        return

    print("Extracting Sequences")
    sequences = get_sequences(files)

    plot_info_list = get_plot_info(on_self, sequences, kmer_size)

    # create plots
    print("Making plots")

    for plot_info in plot_info_list:
        fig, file = CreateDotPlot.create_dot_plot(plot_info[0], plot_info[1], plot_info[2], plot_info[3], kmer_size,
                                                  dot_size)
        fig.savefig(file, dpi=dpi)


def main(args):
    start = time.time()

    kmer_size = int(args['-k'])
    files = args['<files>']
    on_self = args['-s']
    dpi = int(args['-r'])
    dot_size = int(args['-d'])
    vvodka(kmer_size, files, on_self, dpi, dot_size)

    stop = time.time()
    text = f" Time: {stop - start}; Data: {files}; K-mer size: {kmer_size}\n"
    logger(text, "../Logs/VVODKA_timed")


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
