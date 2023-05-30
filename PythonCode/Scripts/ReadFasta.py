#!/usr/bin/python3

"""
ReadFasta.py: Is used to read in fasta files
"""
import pyfastx


def read_fasta(filename):
    """
    Reads fasta files
    :param filename: the name of the to be read file
    :return: A list of all the sequences
    """
    sequences = [i for i in pyfastx.Fasta(filename)]
    return sequences

