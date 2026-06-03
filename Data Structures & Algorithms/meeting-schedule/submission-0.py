"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        holdEnd = intervals[0].end
        for interval in intervals[1:]:
            if holdEnd > interval.start:
                return False
            else:
                holdEnd = interval.end

        return True
