class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.cheapest = float("inf")

        adj = {i: [] for i in range(n)}
        for f, t, price in flights:
            adj[f].append((t, price))

        visited = set()

        def dfs(node, cost, flights_used):
            if cost >= self.cheapest:
                return

            if flights_used > k + 1:
                return

            if node == dst:
                self.cheapest = min(self.cheapest, cost)
                return

            visited.add(node)

            for nei, price in adj[node]:
                if nei not in visited:
                    dfs(nei, cost + price, flights_used + 1)

            visited.remove(node)   # backtracking

        dfs(src, 0, 0)

        return self.cheapest if self.cheapest != float("inf") else -1