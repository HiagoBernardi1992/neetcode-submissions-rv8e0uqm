class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for r, c in prerequisites:
            adj[c].append(r)

        preRqMap = {}
        
        def dfs(c):
            if c not in preRqMap:
                preRqMap[c] = set()
                for r in adj[c]:
                    preRqMap[c] |= dfs(r)
                preRqMap[c].add(c)
            return preRqMap[c]

        for i in range(numCourses):
            dfs(i)

        res = []
        for u, v in queries:
            res.append(u in preRqMap[v])

        return res

        