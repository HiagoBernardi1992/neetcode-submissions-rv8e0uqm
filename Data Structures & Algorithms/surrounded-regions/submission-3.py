class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or board[r][c] != 'O':
                return

            visited.add((r, c))
            board[r][c] = 'N'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):  
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':  
                dfs(r, COLS - 1)           

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == 'N':
                    board[r][c] = 'O'



            