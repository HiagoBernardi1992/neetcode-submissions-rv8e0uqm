class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return False

            visited.add(node)
            for child in graph[node]:
                if child != prevNode:
                    if not dfs(child, node):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)
