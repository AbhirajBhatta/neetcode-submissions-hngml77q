class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dist = -(x*x + y*y)
            heapq.heappush(res, (dist, [x, y]))
            while len(res)>k:
                heapq.heappop(res)
        fin = []
        for item in res:
            fin.append(item[1])
        return fin