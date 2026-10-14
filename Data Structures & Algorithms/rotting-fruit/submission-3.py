class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        fresh_count = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))

        def bfs(r, c):
            nonlocal fresh_count
            if (
                r < 0 or r >= ROWS or c < 0 or c >= COLS or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            fresh_count -= 1
            rotten_queue.append((r, c))

        while rotten_queue and fresh_count > 0:
            qLen = len(rotten_queue)
            minutes += 1
            for i in range(qLen):
                r, c = rotten_queue.popleft()
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
        return minutes if fresh_count == 0 else -1
            
                    



