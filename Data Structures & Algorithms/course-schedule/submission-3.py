class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for c, r in prerequisites:
            adj[c].append(r)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done

        def dfs(c):
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True

            state[c] = 1

            for nei in adj[c]:
                if not dfs(nei):
                    return False

            state[c] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True