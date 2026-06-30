class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for c, r in prerequisites:
            adj[c].append(r)

        state = [0] * numCourses
        res = []

        def dfs(c):
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True

            state[c] = 1
            for r in adj[c]:
                if not dfs(r):
                    return False
            state[c] = 2
            return True

        for c in range(numCourses):
            if dfs(c):
                res.append(c)

        return res

