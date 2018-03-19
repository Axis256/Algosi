class HashTable:
    def __init__(self):
        self.capacity = 28800
        self.table = [None] * self.capacity
        self._collision_count = 0
        self._comp_count = 0
        self._search_count = 0

    def _hash_func(self, value):
        return sum([(ord(c) - 32) for c in (value[0:2] + value[-1])])

    def add(self, value):
        pi = 1600
        n = self.capacity
        i = self._hash_func(value)
        h0 = i
        if len(value) < 3:
            print("Nope")
        if self.table[i] is None or self.table[i] == value:
            self.table[i] = value
        else:
            i = (i + pi) % n
            while i != h0:
                self._collision_count += 1
                if self.table[i] is None or self.table == value:
                    self.table[i] = value
                    break
                else:
                    i = (i + pi) % n
            if i == h0:
                print("Table overflow")

    def find(self, value):
        pi = 1600
        n = self.capacity
        i = self._hash_func(value)
        h0 = i
        self._search_count += 1
        if len(value) < 3:
            print("Sorry")
        if self.table[i] is None:
            return None
        elif self.table[i] == value:
            return i
        else:
            i = (i + pi) % n
            while i != h0:
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
        return self._collision_count