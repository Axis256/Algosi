class Heap:
    def __init__(self, d):
        self.key = []
        self.size = 0
        self.d = d

    def get_parent(self, i):
        return (i - 1) // self.d

    def get_child(self, i, k):
        return i * self.d + k

    def get_last_child(self, i):
        return min(self.size, self.get_child(i, self.d))

    def sift_down(self, i):
        tmp = self.key[i]
        while self.get_child(i, 1) < self.size:
            child = self.min_child(i)
            if self.key[child] < tmp:
                self.key[i] = self.key[child]
                i = child
            else:
                break
        self.key[i] = tmp

    def sift_up(self, i):
        tmp = self.key[i]
        while (i > 0) and (tmp < self.key[self.get_parent(i)]):
            self.key[i] = self.key[self.get_parent(i)]
            i = self.get_parent(i)
        self.key[i] = tmp

    def min_child(self, i):
        min = self.get_child(i, 1)
        k = 2
        tmp = self.get_child(i, k)
        while ((k <= self.d) and (tmp < self.size)):
            if (self.key[tmp] < self.key[min]):
                min = tmp
            k += 1
            tmp = self.get_child(i, k)
        return min

    def insert(self, value):
        self.size += 1
        self.key.append(value)
        self.sift_up(self.size - 1)

    def pop(self):
        if (self.size == 0):
            print("Array underflow")
            return

        self.size -= 1
        tmp = self.key.pop(0)
        if self.size:
            self.sift_down(0)
        return tmp

    def print_heap(self):
        print("Heap = ", end='')
        for i in range(self.size):
            print(self.key[i], end="\t")
        print()
