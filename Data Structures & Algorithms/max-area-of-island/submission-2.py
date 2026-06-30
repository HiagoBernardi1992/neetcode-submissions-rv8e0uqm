class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        res = 0
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res
