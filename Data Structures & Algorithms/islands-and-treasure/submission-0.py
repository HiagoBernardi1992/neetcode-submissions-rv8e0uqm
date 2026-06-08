class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        if ROWS == 0 or COLUMNS == 0:
            return grid

        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        def bfs(prev, r, c):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLUMNS
                or (r, c) in visited
                or grid[r][c] == -1
                or grid[r][c] == 0
            ):
                return
            else:
                grid[r][c] = 1 + prev
                visited.add((r, c))
                q.append((r, c))

        while q:
            r, c = q.popleft()
            bfs(grid[r][c], r + 1, c)
            bfs(grid[r][c], r - 1, c)
            bfs(grid[r][c], r, c + 1)
            bfs(grid[r][c], r, c - 1)

        
