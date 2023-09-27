#!/usr/bin/python3

"""
This script is used to compare different string matching algorithms
"""

from Rabin_karp import rabin_karp
from InlineKmer import find_all
from ReadFasta import read_fasta
from Logger import logger
import time


def main():
    sequences = read_fasta("../../data/Increasing_sized_data/Cflag_c131_50X.fna")

    sequence = sequences[0].seq
    name = sequences[0].name
    sub_len = 1
    subsequence = sequence[0:sub_len]

    find_time = time.time()
    find_finds = find_all(subsequence, sequence)
    find_stop_time = time.time()

    rab_time = time.time()
    rab_finds = rabin_karp(subsequence, sequence)
    rab_stop_time = time.time()

    text = f"Times of different algorithms trying to find all occurrences of a k-mer in a genome.\n" \
           f"Finding subsequence {subsequence} size: {sub_len}, in genome {name}\n" \
           f"Rabin Karp: {rab_stop_time-rab_time}s\n" \
           f"Python Find Time: {find_stop_time - find_time}s\n\n" \
           #f"Rabin Karp hits: {[x for x in rab_finds]}\n" \
           #f"Python find hits: {[x for x in find_finds]}\n\n"
    print(text)
    logger(text, "../Logs/Algorithms_compared")


if __name__ == "__main__":
    main()
