class LinkedKmer:
    def __init__(self, x, y, up, ghost):
        """
        :param x: X coordinate
        :param y: Y coordinate
        :param up: Boolean
        :param ghost: Boolean
        """
        self.x = x
        self.y = y
        self.up = up
        self.ghost = ghost
        self.next_kmer = None
        self.previous_kmer = None

    def __str__(self):
        if self.up:
            direction = "up"
        else:
            direction = "down"
        output = f"x:{self.x}; y:{self.y}; direction:{direction}"
        if self.ghost:
            output += "; is ghost;"
        return output

    def set_next(self, next_kmer):
        self.next_kmer = next_kmer

    def set_previous(self, previous_kmer):
        self.previous_kmer = previous_kmer

    def is_next(self, y):
        if self.up:
            return y == self.y+1
        else:
            return y == self.y-1
