class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        first_col_zero = False

        # 1. marcar
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_zero = True
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 2. aplicar (de trás pra frente é mais seguro)
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, 0, -1):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

            if first_col_zero:
                matrix[r][0] = 0