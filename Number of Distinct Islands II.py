class Solution(object):
    def dfs(self, grid, r, c, shape):
        grid[r][c] = 0
        shape.append((r, c))

        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                self.dfs(grid, nr, nc, shape)

    def normalize(self, shape):
        rotated_shapes = [[] for _ in xrange(8)]
        norm_res = []

        for p in shape:
            x, y = p
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((-x, y))
            rotated_shapes[2].append((x, -y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        for rs in rotated_shapes:
            rs.sort()

        for rs in rotated_shapes:
            tmp = [(0, 0)]
            for i in xrange(1, len(rs)):
                tmp.append((rs[i][0] - rs[0][0], rs[i][1] - rs[0][1]))
            norm_res.append(tmp[:])

        norm_res.sort()

        return tuple(norm_res[0])

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = set()
        for r in xrange(0, m):
            for c in xrange(0, n):
                if grid[r][c] == 1:
                    shape = []
                    self.dfs(grid, r, c, shape)
                    norm = self.normalize(shape)
                    res.add(norm)

        return len(res)