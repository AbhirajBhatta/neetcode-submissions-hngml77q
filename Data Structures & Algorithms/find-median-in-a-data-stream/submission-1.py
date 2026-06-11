class MedianFinder:

    def __init__(self):
        self.minHeap = [] #stores values greater than median
        self.maxHeap = [] #stores values less than median

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.minHeap)>len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)
        elif len(self.maxHeap)>len(self.minHeap)+1:
            val = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2
        