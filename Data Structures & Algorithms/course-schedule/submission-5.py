class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        visited = set()
        state = [0] * numCourses # 0 - 1 - 2
        for c, r in prerequisites:
            adj[c].append(r)

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True

