class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        check_row = [set() for _ in range(9)]
        check_column = [set() for _ in range(9)]
        check_box = [set() for _ in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if board[r][c] in check_row[r]:
                    return False
                check_row[r].add(board[r][c])
                    

                if board[r][c] in check_column[c]:
                    return False
                check_column[c].add(board[r][c])

                box = (r // 3) * 3 + (c // 3)
                if board[r][c] in check_box[box]:
                    return False
                check_box[box].add(board[r][c])

        return True
                    

