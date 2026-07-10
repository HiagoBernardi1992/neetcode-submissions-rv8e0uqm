class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        res = []
        intervalToCheck = intervals[0]
        for interval in intervals:
            if intervalToCheck[1] >= interval[0]:
                intervalToCheck = [min(intervalToCheck[0], interval[0]), max(intervalToCheck[1], interval[1])]
            else:
                res.append(intervalToCheck)
                intervalToCheck = interval

        res.append(intervalToCheck)
        return res