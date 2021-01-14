class Solution(object):
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1])
                    for i in xrange(8)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
                print(len(seen))
                print(N)
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)
        print(seen)
        return cells

    ## 存重复