class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 0:
            return 0
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in adj[node]:
                dfs(child)
       
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count