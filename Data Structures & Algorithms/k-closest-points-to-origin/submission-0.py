class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [math.sqrt((x**2)+(y**2)) for (x, y) in points]
        heap = [(dist, coords) for dist, coords in zip(dist, points)]
        heapq.heapify(heap)
        if k== len(points):
            return points
        res = []
        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res
