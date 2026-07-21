"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals_start = sorted([i.start for i in intervals])
        intervals_end = sorted([i.end for i in intervals])
        count_rooms = 0
        res = 0
        s, e = 0, 0
        while s < len(intervals):
            if intervals_start[s] < intervals_end[e]:
                s += 1
                count_rooms += 1
            else:
                e += 1
                count_rooms -= 1
            res = max(count_rooms, res)

        return res
            
        