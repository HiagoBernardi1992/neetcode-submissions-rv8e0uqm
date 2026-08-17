class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure_positions = deque() 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        inf = 2147483647      
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure_positions.append((r, c))

        while treasure_positions:
            r, c = treasure_positions.popleft()
            for dr, dc in directions:
                newRow, newColumn = r + dr, c + dc

                if (
                    newRow >= 0
                    and newRow < ROWS
                    and newColumn >= 0
                    and newColumn < COLS
                    and grid[newRow][newColumn] == inf
                ):
                    grid[newRow][newColumn] = grid[r][c] + 1
                    treasure_positions.append((newRow, newColumn))