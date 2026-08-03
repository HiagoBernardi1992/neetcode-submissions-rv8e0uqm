class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = []
        target = (ROWS - 1, COLS - 1)
        heapq.heappush(min_heap, [grid[0][0], 0, 0])
        visited = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            if (r, c) == target:
                return val

            for dr, dc in directions:
                new_row, new_column = r + dr, c + dc
                if new_row >= 0 and new_row < ROWS and new_column >= 0 and new_column < COLS and (new_row, new_column) not in visited:
                    visited.add((new_row, new_column))
                    heapq.heappush(min_heap, [max(val, grid[new_row][new_column]), new_row, new_column])
        