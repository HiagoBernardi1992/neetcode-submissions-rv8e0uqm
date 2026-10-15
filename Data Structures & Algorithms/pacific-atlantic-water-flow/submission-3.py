class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0],[-1, 0],[0,1],[0,-1]]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or heights[r][c] < prev:
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, dc + c, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, float("-inf"))
            dfs(ROWS - 1, c, atlantic, float("-inf"))

        for r in range(ROWS):
            dfs(r, 0, pacific, float("-inf"))
            dfs(r, COLS - 1, atlantic, float("-inf"))

        return [[r,c] for r,c in pacific & atlantic]