class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        if ROWS == 0 or COLUMNS == 0:
            return -1

        q = deque()
        fresh = 0
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if  grid[r][c] == 1:
                    fresh += 1

        def bfs(r, c):
            nonlocal fresh
            if (
                r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            fresh -= 1
            q.append((r, c)) 

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
            minutes += 1

        return minutes if fresh == 0 else -1
