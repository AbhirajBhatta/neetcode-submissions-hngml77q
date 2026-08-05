class MedianFinder:

    def __init__(self):
        self.minH, self.maxH = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minH, num)
        if self.minH and self.maxH and self.minH[0] < -self.maxH[0]:
            heapq.heappush(self.maxH, -heapq.heappop(self.minH))
        if len(self.minH)> len(self.maxH)+1:
            heapq.heappush(self.maxH, -heapq.heappop(self.minH))
        if len(self.maxH)> len(self.minH)+1:
            heapq.heappush(self.minH, -heapq.heappop(self.maxH))
        
        


    def findMedian(self) -> float:
        if (len(self.minH)+len(self.maxH))%2==0:
            return (self.minH[0] + -1*self.maxH[0])/2
        else:
            if len(self.minH) > len(self.maxH):
                return self.minH[0]
            else:
                return -self.maxH[0]

        