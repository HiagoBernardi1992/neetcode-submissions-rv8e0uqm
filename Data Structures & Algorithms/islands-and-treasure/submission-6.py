class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if len(grid) < 1 or len(grid[0]) < 1:
            return grid

        ROWS, COLS = len(grid), len(grid[0])
        inf = 2147483647
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if (
                        new_row < 0
                        or new_row == ROWS
                        or new_col < 0
                        or new_col == COLS
                        or (new_row, new_col) in visited
                        or grid[new_row][new_col] != inf
                    ):
                        continue
                    grid[new_row][new_col] = grid[r][c] + 1
                    q.append((new_row, new_col))
