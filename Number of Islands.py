
class Solution(object):
    Length = 0
    width = 0
    num = 0
    def numIslands(self, grid):
        self.Length = len(grid)
        self.width = len(grid[0])
        self.num = 0

        for x in range(self.Length):
            for y in range(self.width):
                if grid[x][y] == 1:
                    self.find(x, y, grid)
                    self.num += 1
        return self.num
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    def find(self, x, y, grid):
        if x < 0 or y < 0 or x == self.Length or y == self.width:
            return
        if grid[x][y] == 1:
            grid[x][y] == 0
            self.find(x - 1, y + 1, grid)
            self.find(x - 1, y - 1, grid)
            self.find(x + 1, y + 1, grid)
            self.find(x + 1, y - 1, grid)
        return
