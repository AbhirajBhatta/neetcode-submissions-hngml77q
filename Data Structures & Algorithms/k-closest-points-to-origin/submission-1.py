class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dist = x**2 + y**2
            if len(res) < k:
                heapq.heappush(res, (-dist, (x, y)))
            else:
                if dist < -res[0][0]:
                    heapq.heappop(res)
                    heapq.heappush(res, (-dist, (x, y)))
        return [item[1] for item in res]

