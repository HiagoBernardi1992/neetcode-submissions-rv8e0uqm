class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        state = [0] * n
        visited = set()

        def dfs(node, prev):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            visited.add(node)
            state[node] = 1
            for n in adj[node]:
                if n != prev:
                    if not dfs(n, node):
                        return False

            state[node] = 2
            return True

        return True if dfs(0, None) and len(visited) == n else False