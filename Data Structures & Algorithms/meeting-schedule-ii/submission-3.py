"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        s, e = 0, 0
        count = 0
        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(count, res)

        return res