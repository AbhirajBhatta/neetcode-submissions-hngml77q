class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxH, [-1*dist, (x, y)])
            if len(maxH)>k:
                heapq.heappop(maxH)
        res = [[x, y] for dist, [x, y] in maxH]
        return res