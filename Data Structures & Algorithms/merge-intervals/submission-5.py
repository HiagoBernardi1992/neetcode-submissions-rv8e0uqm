class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda i : i[0])

        res = []
        oldInterval = intervals[0]
        for i in range(1, len(intervals)):
            if oldInterval[1] >= intervals[i][0]:
                oldInterval = [min(oldInterval[0], intervals[i][0]), max(oldInterval[1], intervals[i][1])]
            else:
                res.append(oldInterval)
                oldInterval = intervals[i]

        res.append(oldInterval)
        return res
