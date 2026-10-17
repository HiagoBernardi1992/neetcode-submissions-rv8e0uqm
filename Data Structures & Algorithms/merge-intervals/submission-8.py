class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        res = []
        intervalsToCheck = intervals[0]
        for i in range(1, len(intervals)):
            if intervalsToCheck[1] >= intervals[i][0]:
                intervalsToCheck = [min(intervalsToCheck[0], intervals[i][0]), max(intervalsToCheck[1], intervals[i][1])]
            else:
                res.append(intervalsToCheck)
                intervalsToCheck = intervals[i]

        res.append(intervalsToCheck)
        return res