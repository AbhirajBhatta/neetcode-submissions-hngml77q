class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)

                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # adj is a mapping of points to [distance, another point]
        visited = set()
        minheap = [[0, 0]]
        res = 0
        while len(visited) < N:
            dist, point = heapq.heappop(minheap)
            if point in visited:
                continue
            res += dist
            visited.add(point)
            for distNei, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minheap, [distNei, nei])
        return res