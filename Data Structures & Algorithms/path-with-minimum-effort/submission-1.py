class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        target = (ROWS - 1, COLS - 1)
        visited = set()
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        min_heap = []
        heapq.heappush(min_heap, [0, 0, 0])
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            visited.add((r,c))

            if (r,c) == target:
                return diff
            
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS and (new_row, new_col) not in visited:
                    new_diff = max(diff, abs(heights[r][c] - heights[new_row][new_col]))
                    heapq.heappush(min_heap, [new_diff, new_row, new_col])
            
