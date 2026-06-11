class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        for c, r in prerequisites:
            adj[c].append(r)

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if adj[c] == []:
                return True

            visited.add(c)
            for r in adj[c]:
                if not dfs(r):
                    return False
            visited.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        

        