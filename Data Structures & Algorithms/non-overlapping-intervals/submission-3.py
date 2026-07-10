class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort()
        end_interval = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if end_interval > intervals[i][0]:
                count += 1
                end_interval = min(end_interval, intervals[i][1])
            else:
                end_interval = intervals[i][1]

        return count

        

        
        

                


        