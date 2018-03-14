class HashTable:
    def __init__(self):
        self.capacity = 288
        self.table = [None] * self.capacity
        self._collision_count = 0
        self._comp_count = 0
        self._search_count = 0

    def _hash_func(self, value):
        chr1 = value[0]
        chr2 = value[1]
        chr3 = value[len(value) - 1]
        return ord(chr1) + ord(chr2) + ord(chr3) - 32 * 3

    def add(self, value):
        pi = 16
        n = self.capacity
        i = self._hash_func(value)
        h0 = i
        if self.table[i] is None or self.table[i] == value:
            self.table[i] = value
        else:
            i = (i + pi) % n
            while i != h0:
                if self.table[i] is None or self.table == value:
                    self.table[i] = value
                    break
                else:
                    i = (i + pi) % n
            if i == h0:
                print("Table overflow")

    def find(self, value):
        pi = 16
        n = self.capacity
        i = self._hash_func(value)
        h0 = i
        self._search_count += 1
        if self.table[i] is None:
            return None
        elif self.table[i] == value:
            return i
        else:
            i = (i + pi) % n
            while i != h0:
                self._collision_count += 1
                self._comp_count += 1
                if self.table[i] is None:
                    return None
                elif self.table[i] == value:
                    return i
                else:
                    i = (i + pi) % n
            if i == h0:
                return None

    def avg_comp(self):
        return self._comp_count / self._search_count

    def avg_collisions(self):
        return self._collision_count / self._search_count