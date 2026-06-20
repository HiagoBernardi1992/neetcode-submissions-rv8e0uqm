"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 0:
            return False
        lastEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if lastEnd > intervals[i].end:
                return False
            else:
                lastEnd = max(lastEnd, intervals[i].end)

        return True
