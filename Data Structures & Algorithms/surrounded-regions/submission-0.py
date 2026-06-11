class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[0])
        if ROWS == 0 or COLUMNS == 0:
            return

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or board[r][c] != "O":
                return
            board[r][c] = "N"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        edges = set()
        for c in range(COLUMNS):
            if board[0][c] == "O":
                edges.add((0, c))
            if board[ROWS - 1][c] == "O":
                edges.add((ROWS - 1, c))

        for r in range(ROWS):
            if board[r][0] == "O":
                edges.add((r, 0))
            if board[r][COLUMNS - 1] == "O":
                edges.add((r, COLUMNS - 1))

        for r, c in edges:
            dfs(r, c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
                    
