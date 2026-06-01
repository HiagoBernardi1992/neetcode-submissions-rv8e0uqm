class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda i : i[0])

        res = []
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            if newInterval[1] >= intervals[i][0]:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            else:
                res.append(newInterval)
                newInterval = intervals[i]
        
        res.append(newInterval)
        return res
