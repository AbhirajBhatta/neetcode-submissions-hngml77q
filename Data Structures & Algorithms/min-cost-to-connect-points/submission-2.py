class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minH = [[0, 0]]
        visited = set()

        cost = 0
        while minH:
            c, point = heapq.heappop(minH)
            if point in visited:
                continue
            visited.add(point)
            cost += c
            for neiC, neiPoint in adj[point]:
                if neiPoint not in visited:
                    heapq.heappush(minH, [neiC, neiPoint])
        return cost
