#!/usr/bin/python3

# TODO add merge option
# TODO create main script that only handles the docopt and passing of arguments, change this script to only contain
#  functions that can be used as imports

usage = """
Main.py: Main.py is used to handle the user input, call the right functions and return the final output

Usage:
    Main.py -k <kmer_size> [-r <dpi>] [-s <self>] [-d <dot_size>] <files>...
    Main.py (-h | --help | --version)
    
Options:
    -k <kmer_size>  Specify the size of the k-mer
    -r <dpi>        Specify the DPI [default: 600]
    -s <self>       Specify if files should be plotted against themselves, use Y to plot against itself or N to not 
                    plot against itself [default: Y]
    -d <dot_size>   Specify the dot size to be used in the dot plot [default: 2]
    <files>...      Specify the files which are plotted against each other
"""

__author__ = "Gijs Bakker"
__version__ = 0.5

from docopt import docopt
import InlineKmer
import FastaSequence
import CreateDotPlot
import ReadFasta


def main(args):
    """
    This validates all given arguments
    :param args: docopt arguments
    """

    # TODO change code for these
    merged_files = []

    kmer_size = int(args['-k'])
    files = args['<files>']
    on_self = args['-s']
    dpi = int(args['-r'])
    dotsize = int(args['-d'])

    # Check if arguments are correctly specified
    if on_self.upper() not in ['Y', 'N']:
        print("Please set -s to either Y or N")
        return
    if on_self.upper() == 'N' and len(files) <= 1:
        print("No plots to make, make sure that you specify multiple files when using -s=N")
        return

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

    # should compare all files
    indexes = [i for i in range(len(sequences))]

    # TODO can be its own function until the positions are filled
    # check if plot against self should be made
    if on_self:
        start = 0
    else:
        start = 1

    plot_info_list = []

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

    # create plots
    print("Making plots")

    for plot_info in plot_info_list:
        fig, file = CreateDotPlot.create_dot_plot(plot_info[0], plot_info[1], plot_info[2], plot_info[3], kmer_size,
                                                  dotsize)
        fig.savefig(file, dpi=dpi)


if __name__ == '__main__':
    args = docopt(usage)
    main(args)
