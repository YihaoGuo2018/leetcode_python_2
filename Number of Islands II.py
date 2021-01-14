class UnionFind(object):
    def __init__(self, m, n, positions):
        self.n = n
        self.size = [0] * (m * n)
        self.id = [None] * (m * n)
        self.count = 0

    def genIndex(self, i, j):
        return self.n * i + j

    def add(self, i, j):
        index = self.genIndex(i, j)

        self.size[index] = 1
        self.id[index] = index
        self.count += 1

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp, idq = map(self.find, (p, q))
        if idp == idq:
            return

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]

        self.count -= 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        uf, r = UnionFind(m, n, positions), []

        for i, j in positions:
            uf.add(i, j)
            index = uf.genIndex(i, j)

            neighbors = zip(
                (j > 0, i > 0, j + 1 < n, i + 1 < m),
                (uf.genIndex(x, y) for x, y in ((i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)))
            )

            [uf.union(index, neighbor) for condition, neighbor in neighbors
             if condition and uf.id[neighbor] is not None]

            r.append(uf.count)

        return r