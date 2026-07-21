class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        for r, c in prerequisites:
            adj[c].append(r)

        visited = set()
        res = []

        def dfs(course, requisite_find):
            if course in visited:
                return False

            if course == requisite_find:
                return True

            visited.add(course)
            for nei in adj[course]:
                if dfs(nei, requisite_find):
                    return True

            visited.remove(course)

            return False

        for r, c in queries:
            res.append(dfs(c, r))

        return res


            



        