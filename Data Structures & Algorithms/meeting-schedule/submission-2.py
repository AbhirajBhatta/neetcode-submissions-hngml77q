"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def getStart(interval):
    return interval.start
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = 0
        intervals.sort(key=getStart)
        for i in intervals:
            if i.start < prevEnd:
                return False
            prevEnd = i.end
        return True