#!/usr/bin/python3

"""
ReadFasta.py: Is used to read in fasta files
"""

from Bio import SeqIO


def read_fasta(filename):
    # TODO could be more than one sequence?
    sequences = [i for i in SeqIO.parse(filename, "fasta")]
    seq = sequences[0]
    return seq

