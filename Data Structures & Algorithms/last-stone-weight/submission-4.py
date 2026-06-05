class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x==y:continue
            heapq.heappush(heap, -1*(x-y))
        return -1*heap[0] if heap else 0
