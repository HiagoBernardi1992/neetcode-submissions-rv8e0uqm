class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLUMNS = len(heights), len(heights[0])
        minHeap = [[0,0,0]] #[diff, r, c]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == ROWS - 1 and c == COLUMNS - 1:
                return diff

            for dr, dc in directions:
                newRow = r + dr
                newColumn = c + dc
                if newRow < 0 or newRow == ROWS or newColumn < 0 or newColumn == COLUMNS or (newRow, newColumn) in visited:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newRow][newColumn]))
                heapq.heappush(minHeap, [newDiff, newRow, newColumn])