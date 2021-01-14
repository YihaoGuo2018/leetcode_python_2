def updateBoard(self, A, click):
    click = tuple(click)
    R, C = len(A), len(A[0])

    def neighbors(r, c):
        for dr in xrange(-1, 2):
            for dc in xrange(-1, 2):
                if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                    yield r + dr, c + dc

    stack = [click]
    seen = {click}
    while stack:
        r, c = stack.pop()
        if A[r][c] == 'M':
            A[r][c] = 'X'
        else:
            mines_adj = sum(A[nr][nc] in 'MX' for nr, nc in neighbors(r, c))
            if mines_adj:
                A[r][c] = str(mines_adj)
            else:
                A[r][c] = 'B'
                for nei in neighbors(r, c):
                    if A[nei[0]][nei[1]] in 'ME' and nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
    return A