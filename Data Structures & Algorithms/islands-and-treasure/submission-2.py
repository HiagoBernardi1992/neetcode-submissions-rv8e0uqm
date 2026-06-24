class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 0:
                    q.append((r, c))

        def bfs(r, c, count):
            if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or grid[r][c] != 2147483647:
                return
            
            grid[r][c] = count
            q.append((r, c))

        counter = 0
        while q:
            qLen = len(q)
            counter += 1
            for i in range(qLen):
                r, c = q.popleft()
                bfs(r + 1, c, counter)
                bfs(r - 1, c, counter)
                bfs(r, c + 1, counter)
                bfs(r, c - 1, counter)



        
