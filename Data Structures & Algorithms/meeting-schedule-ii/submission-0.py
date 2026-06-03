"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 0:
            return len(intervals)

        numberOfRooms = 1

        intervals.sort(key = lambda i : i.start)
        holdEnd = intervals[0].end
        for interval in intervals[1:]:
            if holdEnd > interval.start:
                numberOfRooms += 1
            holdEnd = interval.end

        return numberOfRooms
        