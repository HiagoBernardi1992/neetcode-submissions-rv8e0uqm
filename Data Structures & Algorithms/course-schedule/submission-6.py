class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        state = [0] * numCourses # 0 init - 1 visiting - 2 can conclued
        for course, requisite in prerequisites:
            adj[course].append(requisite)

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

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        
