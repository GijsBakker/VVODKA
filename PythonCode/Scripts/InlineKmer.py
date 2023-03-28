from LinkedKmer import LinkedKmer


def find_all(sub, a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)   # use start += 1 to find overlapping matches


def invert_kmer(kmer):

    #\X01 : C
    #\X02 : G
    #\X03 : T
    #\X00 : A

    bin_dict = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
    invert_dict = {
        3: 0b00,
        0: 0b11,
        1: 0b10,
        2: 0b01
    }
    inverted_kmer = bytearray('', encoding='utf-8')
    for byte in kmer:
        inverted_kmer.append(invert_dict[byte])

    return inverted_kmer


def find_overlap_kmers(seq1, seq2, kmer_length, wanted_length, max_misses):
    # TODO object instead of list
    # TODO shorten code if possible
    possible_kmers = []
    final_kmers = []

    for x_pos in range(len(seq1) - kmer_length + 1):
        kmer = seq1[x_pos:x_pos + kmer_length]
        kmer_rev = kmer[::-1]
        # kmer_rev = invert_kmer(kmer[::-1])
        y_kmers = []
        x_kmers = []
        if kmer in seq2:
            y_kmers += [y_pos for y_pos in find_all(kmer, seq2)]
            x_kmers += [x_pos for y_pos in range(len(y_kmers))]
        if kmer_rev in seq2 and kmer != kmer_rev:
            y_kmers += [y_pos for y_pos in find_all(kmer_rev, seq2)]
            x_kmers += [x_pos for y_pos in range(len(y_kmers))]

        new_kmers = list(zip(x_kmers, y_kmers))
        to_be_deleted = []
        # Check per existing kmer if a newfound kmer fits on it
        for kmer in possible_kmers:
            if not kmer[1] in new_kmers:     # if not found add one miss
                kmer[2] += 1    # +1 misses

            kmer[1] = (kmer[1][0] + 1, kmer[1][1] + kmer[4])  # update next wanted kmer.
            kmer[3] += 1  # +1 len

            if kmer[2] > max_misses:
                to_be_deleted.append(kmer)
            elif kmer[3] >= wanted_length:
                final_kmers.append(kmer[0])
                to_be_deleted.append(kmer)

        # remove to be deleted kmers
        for kmer in to_be_deleted:
            possible_kmers.remove(kmer)

        # Add new kmer up and down
        for kmer in new_kmers:
            possible_kmers.append([kmer, (kmer[0]+1, kmer[1]+1), 0, 1, 1])
            possible_kmers.append([kmer, (kmer[0]+1, kmer[1]-1), 0, 1, -1])

    return final_kmers


def unzip_kmers(kmer_list):
    return list(zip(*kmer_list))


def find_overlapping_kmers(seq1, seq2, kmer_length, wanted_length, max_misses):
    zipped = find_overlap_kmers(seq1, seq2, kmer_length, wanted_length, max_misses)
    unzipped = unzip_kmers(zipped)
    return [list(unzipped[0]), list(unzipped[1])]
