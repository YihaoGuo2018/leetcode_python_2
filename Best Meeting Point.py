class Solution(object):
    def minTotalDistance(self, grid):
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        sumr = [i for i in xrange(r) for j in xrange(c) if grid[i][j]]
        sumc = [j for i in xrange(r) for j in xrange(c) if grid[i][j]]
        sumr.sort()
        sumc.sort()
        mid_row = sumr[len(sumr)/2]
        mid_col = sumc[len(sumc)/2]
        return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])