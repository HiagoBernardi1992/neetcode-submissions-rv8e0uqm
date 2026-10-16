class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                if nei != prev:
                    dfs(nei, node)
            
            return

        connect_count = 0

        for e in range(n):
            if e not in visited:
                connect_count += 1
                dfs(e, None)

        return connect_count
