class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                if n >= heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
        
        while len(heap) != k:
            heapq.heappop(heap)
        return heap[0]