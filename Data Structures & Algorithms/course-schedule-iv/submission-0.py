class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for r, c in prerequisites:
            adj[c].append(r)

        res = []
        def dfs(c, r):
            if not adj[c]:
                return False
            
            if r in adj[c]:
                return True
            
            for rq in adj[c]:
                return dfs(rq, r)

        for r, c in queries:
            res.append(dfs(c, r))

        return res

        