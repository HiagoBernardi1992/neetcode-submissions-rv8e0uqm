class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for c, r in prerequisites:
            adj[c].append(r)

        state = [0] * numCourses

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
            if not dfs(c):
                return False


        return True

