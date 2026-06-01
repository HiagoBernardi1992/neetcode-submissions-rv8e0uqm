class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda i : i[0])

        res = []
        holdinterval = intervals[0]
        for i in range(1, len(intervals)):
            if holdinterval[1] >= intervals[i][0]:
                holdinterval = [min(holdinterval[0], intervals[i][0]), max(holdinterval[1], intervals[i][1])]
            else:
                res.append(holdinterval)
                holdinterval = intervals[i]
        
        res.append(holdinterval)
        return res
