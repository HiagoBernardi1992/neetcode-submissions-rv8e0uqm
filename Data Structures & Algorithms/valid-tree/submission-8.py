class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        state = [0] * n
        concluded = set()

        def dfs(node, prev):
            if state[node] == 2:
                return True
            if state[node] == 1:
                return False
            state[node] = 1
            for nei in adj[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            state[node] = 2
            concluded.add(node)
            return True

        if not dfs(0, None):
            return False

        return True if len(concluded) == n else False
        