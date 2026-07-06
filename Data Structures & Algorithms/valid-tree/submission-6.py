class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        state = [0] * n

        def dfs(node, prev):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for n in adj[node]:
                if n != prev:
                    if not dfs(n, node):
                        return False

            state[node] = 2
            return True

        for edge in range(n):
            if not dfs(edge, None):
                return False

        return True
