class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        number_islands = 0

        def dfs(r, c):
            if (r,c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0":
                return

            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    number_islands += 1
                    dfs(r,c)

        return number_islands