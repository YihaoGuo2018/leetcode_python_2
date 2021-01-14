from collections import deque
class Solution(object):

    def shortestDistance(self, maze, start, destination):

        if not maze or not maze[0] or start == destination:
                return 0

        M, N = len(maze[0]), len(maze)
        visited = {(start[0], start[1]): 0}
        queue = deque([(start[0], start[1], 0)])

        while queue:
                i, j, dist = queue.popleft()

                # directions
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x, y, d = i, j, dist
                        while 0<=x+dx<N and 0<=y+dy<M and maze[x+dx][y+dy] == 0:
                                x += dx
                                y += dy
                                d += 1
                        if (x, y) not in visited or ((x, y) in visited and visited[(x,y)] > d):
                                visited[(x, y)] = d
                                if (x, y) != (destination[0], destination[1]) :
                                        queue.append((x, y, d))
        return visited.get((destination[0], destination[1]), -1)