class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dp = {}

        def dfs(r, c, prev):
            
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev:
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 0
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                res = max(res, 1 + dfs(new_row, new_col, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(dp.values())
            
