class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        adj = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        countEdges = {}
        leaves = deque()
        for edge, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(edge)
            countEdges[edge] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    countEdges[nei] -= 1
                    if countEdges[nei] == 1:
                        leaves.append(nei)

