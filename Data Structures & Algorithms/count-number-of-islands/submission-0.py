class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        visited = set()
        numberOfIsland = 0

        def dfs(r, c):

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLUMNS or
                (r, c) in visited or
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

                if grid[r][c] == "1" and (r, c) not in visited:
                    numberOfIsland += 1
                    dfs(r, c)

        return numberOfIsland