class MedianFinder:

    def __init__(self):
        self.small, self.big = [], [] #smaller is a maxH, bigger is a minH
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.big and -self.small[0]>self.big[0]:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.small) > len(self.big)+1:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.big) > len(self.small)+1:
            heapq.heappush(self.small, -heapq.heappop(self.big))
        
    def findMedian(self) -> float:
        if len(self.big)<len(self.small):
            return -self.small[0]
        elif len(self.big)>len(self.small):
            return self.big[0]
        return (self.big[0] + -self.small[0])/2

        
        