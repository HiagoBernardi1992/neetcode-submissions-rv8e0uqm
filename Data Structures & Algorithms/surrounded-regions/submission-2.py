class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLUMNS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or board[r][c] != "O":
                return

            board[r][c] = "N"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # bordas diretamente
        for c in range(COLUMNS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLUMNS - 1)

        # flip final
        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"