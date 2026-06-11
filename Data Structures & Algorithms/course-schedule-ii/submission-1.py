class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i : [] for i in range(numCourses) }
        for c, r in prerequisites:
            adj[c].append(r)
        
        res = []
        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done

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
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res

         
