class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        if ROWS == 0 or COLUMNS == 0:
            return 0

        numberOfIsland = 0
        visited = set()

        def dfs(r, c):

            if (
                (r, c) in visited or
                r < 0 or r == ROWS or
                c < 0 or c == COLUMNS or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r, c) not in visited and grid[r][c] == "1":
                    numberOfIsland += 1
                    dfs(r, c)

        return numberOfIsland