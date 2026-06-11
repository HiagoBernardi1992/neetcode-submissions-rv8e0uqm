class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLUMNS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLUMNS
                or (r, c) in visited
                or heights[r][c] < prev
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLUMNS):
            dfs(0, c, pacific, float("-inf"))
            dfs(ROWS - 1, c, atlantic, float("-inf"))

        for r in range(ROWS):
            dfs(r, 0, pacific, float("-inf"))
            dfs(r, COLUMNS - 1, atlantic, float("-inf"))

        return [[r, c] for r, c in pacific & atlantic]