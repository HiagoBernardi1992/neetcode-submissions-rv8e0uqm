class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        inf = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                newRow, newColumn = r + dr, c + dc

                if (
                    newRow >= 0
                    and newRow < ROWS
                    and newColumn >= 0
                    and newColumn < COLS
                    and grid[newRow][newColumn] == inf
                ):
                    grid[newRow][newColumn] = grid[r][c] + 1
                    q.append((newRow, newColumn))
