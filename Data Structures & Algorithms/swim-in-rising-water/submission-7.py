class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        min_heap = []
        heapq.heappush(min_heap, [grid[0][0], 0, 0])
        target = (ROWS - 1, COLS - 1)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            if (r, c) == target:
                return height

            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if (
                    new_row < 0
                    or new_row == ROWS
                    or new_col < 0
                    or new_col == COLS
                    or (new_row, new_col) in visited
                ):
                    continue
                visited.add((r, c))
                heapq.heappush(min_heap, [max(height, grid[new_row][new_col]), new_row, new_col])
