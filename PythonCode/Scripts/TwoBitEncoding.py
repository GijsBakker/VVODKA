#!/usr/bin/python3

"""
2bitEncoding: Is used to compress dna strings to each nucleotide being represented with just two bits
"""

bin_dict = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}


def string_to_two_bit(sequence):
    """
    This function compresses a DNA sequence to a two bit sequence. It assumes the given sequence contains only dna
    :param sequence: A string representation of a dna sequence
    :return: A compressed string as a bytearray
    """
    compressed = bytearray('', encoding='utf-8')
    for nucleotide in sequence:
        compressed.append(bin_dict[nucleotide])
    return compressed
