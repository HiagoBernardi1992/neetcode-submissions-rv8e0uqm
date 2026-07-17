class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        res = 0
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        for n in range(n):
            if n not in visited:
                res += 1
                dfs(n)

        return res