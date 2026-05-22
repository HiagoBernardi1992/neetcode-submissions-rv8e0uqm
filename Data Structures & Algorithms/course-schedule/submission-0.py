class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapCourseRequisites = {i: [] for i in range(numCourses)}
        for c, r in prerequisites:
            mapCourseRequisites[c].append(r)
        visiting = set()
        done = set()

        def dfs(c):
            if c in done:
                return True
            if c in visiting:
                return False

            visiting.add(c)
            for r in mapCourseRequisites[c]:
                if not dfs(r):
                    return False
            visiting.remove(c)
            done.add(c)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
