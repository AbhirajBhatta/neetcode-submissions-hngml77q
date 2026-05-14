class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        while len(maxheap)>1:
            x, y = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
            if x!=y:
                heapq.heappush(maxheap, -(x-y))
        return -maxheap[0] if maxheap else 0