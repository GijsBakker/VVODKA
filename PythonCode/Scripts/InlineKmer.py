from LinkedKmer import LinkedKmer


def find_all(sub, a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)   # use start += 1 to find overlapping matches


# def find_overlap_kmers(seq1, seq2, kmer_length):
#     final_kmers = []
#     found_kmers = []
#     linked_kmers_list = []
#
#     # After each iteration of x_pos all found overlapping kmers need to be added to a list of linked lists
#     #   Both the upward and downward linked list need to be added.
#     # After each iteration:
#     #   For each item in the linked list check if a new linked list y is either one higher or lower based on direction
#     #       If so add it after the linked list
#     #       If not add Ghost kmer and add one miss to all elements in the linked list
#     #   Check if one has more misses than allowed. If so remove the element. And check same for next element
#     #       If next element is ghost remove it even if it has no misses
#     #   Check if one has a length of consecutive kmers that is needed. If so add to final_kmer_list and remove it from
#     #       linked list. Not if it is a ghost kmer
#
#     # EXAMPLE LINKED LIST: <X, Y, M, Up/Down, Ghost, Before, After>
#     #   should also contain get length function
#
#     for x_pos in range(len(seq1) - kmer_length + 1):
#         kmer = seq1[x_pos:x_pos + kmer_length]
#         kmer_rev = kmer[::-1]
#         if kmer in seq2:
#             y_kmers = [y_pos for y_pos in find_all(kmer, seq2)]
#             x_kmers = [x_pos for y_pos in range(len(y_kmers))]
#             found_kmers += list(zip(x_kmers, y_kmers))
#
#         if kmer_rev in seq2 and kmer != kmer_rev:
#             y_kmers = [y_pos for y_pos in find_all(kmer_rev, seq2)]
#             x_kmers = [x_pos for y_pos in range(len(y_kmers))]
#             found_kmers += list(zip(x_kmers, y_kmers))
#
#         for linked_kmers in linked_kmers_list:
#             for kmer in found_kmers:
#                 if linked_kmers[-1].is_next(kmer[1]):
#                     linked_kmers.apped(LinkedKmer(kmer[0], kmer[1], linked_kmers[-1].up, False))
#                     break   # because direction is given only one can fit
#
#         # add all non added to the end
#
#         # check which ones should be added
#
#     return found_kmers


def find_overlap_kmers(seq1, seq2, kmer_length):
    found_kmer_list = []

    for x_pos in range(len(seq1) - kmer_length + 1):
        kmer = seq1[x_pos:x_pos + kmer_length]
        kmer_rev = kmer[::-1]
        if kmer in seq2:
            y_kmers = [y_pos for y_pos in find_all(kmer, seq2)]
            x_kmers = [x_pos for y_pos in range(len(y_kmers))]
            found_kmer_list += list(zip(x_kmers, y_kmers))
        if kmer_rev in seq2 and kmer != kmer_rev:
            y_kmers = [y_pos for y_pos in find_all(kmer_rev, seq2)]
            x_kmers = [x_pos for y_pos in range(len(y_kmers))]
            found_kmer_list += list(zip(x_kmers, y_kmers))

    return found_kmer_list


def unzip_kmers(kmer_list):
    return list(zip(*kmer_list))


def find_overlapping_kmers(seq1, seq2, kmer_length):
    zipped = find_overlap_kmers(seq1, seq2, kmer_length)
    unzipped = unzip_kmers(zipped)
    return [list(unzipped[0]), list(unzipped[1])]
