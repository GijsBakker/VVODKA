# #!/usr/bin/python3
#
# """
# KMer.py: Is used to find k-mers in genomes
# """
#
# __author__ = "Gijs Bakker"
# __version__ = 0.1
#
#
# import math
# import re
# import time
#
# import multiprocessing as mp
# from Scripts import Main
#
#
# def find_kmer(k_mer, kmers_two):
#     """
#     This function compare looks for a k-mer within a sequence
#     :param k_mer:
#     :param kmers_two:
#     :return: a list of the positions of the found kmers
#     """
#     return [idx for idx, value in enumerate(kmers_two) if value == k_mer]
#
#
# def sequence_to_kmer_dict(sequence, kmer_size):
#     # uses dictionary since then you don't have to have N kmers but a max of 4^kmer_size
#     # and later you can easily spot which kmer occurs often for removing non informative kmers
#     # search speed increases
#     kmers = {}
#     for start in range(len(sequence) - kmer_size+1):
#         kmer = sequence[start:start+kmer_size]
#         kmer = sorted([kmer, kmer[::-1]])[0]
#         if kmers.get(kmer):
#             kmers[kmer] = kmers.get(kmer) + [start]
#         else:
#             kmers[kmer] = [start]
#     return kmers
#
#
# def find_group_kmers(kmers_one, kmers_two, start_pos_x):
#     """
#     This function takes a group of kmers and find all those kmers in the given sequence
#     :param start_pos_x: The position of these kmers within the first sequence
#     :param kmers_one:
#     :param kmers_two:
#     :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
#     """
#     pos_y = []
#     pos_x = []
#
#     for kmer_number, kmer in enumerate(kmers_one):
#         found_kmers = find_kmer(kmer, kmers_two)
#         pos_y += found_kmers
#         pos_x += [start_pos_x + kmer_number for i in range(len(found_kmers))]
#
#     return [pos_x, pos_y]
#
#
# def multi_run_wrapper(args):
#     """
#     This function is a way to have multiple arguments in one multiprocess call
#     :param args: The arguments from a multiprocess function call
#     :return: a list of the x and y positions [[x1,x2,..], [y1,y2,...]]
#     """
#     return find_group_kmers(*args)
#
#
# def multi_process(cores, kmers_one, kmers_two):
#     """
#     This function finds given kmers in a sequence. It does this in a way that supports using multiple cores.
#     :param cores: number of cores
#     :param kmers_one:
#     :param kmers_two:
#     :return: The found positions within a list: [[x1,x2,...], [y1,y2,...]]
#     """
#     # split kmers in equal groups
#     kmer_range = math.floor(len(kmers_one) / cores)
#     kmer_groups = []
#     if kmer_range >= 1:
#         for i in range(cores-1):
#             print(dict(list(kmers_one.items())[i * kmer_range: (i + 1) * kmer_range]))
#             kmer_groups.append(dict(list(kmers_one.items())[i * kmer_range: (i + 1) * kmer_range]))
#
#     # add last group which is smaller
#     kmer_groups.append(dict(list(kmers_one.items())[(cores - 1) * kmer_range: len(kmers_one)]))
#
#     pos_x = []
#     pos_y = []
#
#     # multi Processed
#     p = mp.Pool(processes=cores)
#     args = [[kmer_group, kmers_two, start_pos_x * kmer_range] for start_pos_x, kmer_group in enumerate(kmer_groups)]
#     all_data = p.map(multi_run_wrapper, args)
#
#     # unpack data for each run
#     for data in all_data:
#         pos_x += data[0]
#         pos_y += data[1]
#
#     return [pos_x, pos_y]
#
#
# def find_overlapping_kmers(sequence_one, sequence_two, size, cores):
#     """
#     This function finds the overlapping kmers between two sequences.
#     :param sequence_one: bytearray of the first sequence
#     :param sequence_two: bytearray of the second sequence
#     :param size: size of the kmers. Cannot be smaller than 1
#     :return: The found positions within a list: [[x1,x2,...], [y1,y2,...]]
#     """
#     print("Getting K-mers")
#     kmer_dict_one = sequence_to_kmer_dict(sequence_one, size)
#     kmer_dict_two = sequence_to_kmer_dict(sequence_two, size)
#
#     print("Searching for matches")
#     positions_x, positions_y = multi_process(cores, kmer_dict_one, kmer_dict_two)
#     overlap_positions = [positions_x, positions_y]
#     return overlap_positions
