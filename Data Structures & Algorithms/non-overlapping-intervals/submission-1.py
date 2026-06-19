class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 0:
            return 0

        intervals.sort(key = lambda i : i[0])
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
                prevEnd = max(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        return count

        
        

                


        