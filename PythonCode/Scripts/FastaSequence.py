#!/usr/bin/python3

"""
FastaSequence.py: Is used to create fastaSequences when combining sequences
"""

import TwoBitEncoding


class FastaSequence:
    def __init__(self, name, sequence):
        self.name = name
        self.seq = TwoBitEncoding.string_to_two_bit(sequence)
