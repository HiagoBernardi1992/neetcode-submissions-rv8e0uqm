class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLUMNS = len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prevH):
            if (
                r < 0 or c < 0
                or r == ROWS or c == COLUMNS
                or (r, c) in visited
                or heights[r][c] < prevH
                ): return
            visited.add((r,c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            

        for c in range(COLUMNS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLUMNS - 1, atl, heights[r][COLUMNS - 1])

        for (r, c) in pac:
            if (r, c) in atl:
                res.append([r,c])

        return res
        
        