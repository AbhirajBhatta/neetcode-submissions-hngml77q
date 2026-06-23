class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minH = [[0, 0]]
        visited = set()
        path = 0
        while minH:
            dist, point = heapq.heappop(minH)
            if point in visited:
                continue
            visited.add(point)
            path+=dist
            for neiDist, neiPoint in adj[point]:
                if neiPoint not in visited:
                    heapq.heappush(minH, [neiDist, neiPoint])
        return path