from collections import deque


class LinkedKmerList:
    def __init__(self, kmer):
        self.kmer_list = deque(kmer)

    def remove_first(self):
        self.kmer_list.popleft()

    def get_first(self):
        return self.kmer_list[0]

    def get_last(self):
        return self.kmer_list[-1]

    def __add__(self, other):
        self.kmer_list.append(other)
