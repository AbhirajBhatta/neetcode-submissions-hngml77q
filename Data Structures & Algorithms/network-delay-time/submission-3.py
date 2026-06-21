class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}

        for u, v, w in times:
            adj[u].append((v, w))
        
        visited = set()
        minheap = [[0, k]]
        minDist = 0
        while minheap:
            w1, v1 = heapq.heappop(minheap)
            if v1 in visited:
                continue
            mindist = max(minDist, w1)
            visited.add(v1)
            for v2, w2 in adj[v1]:
                if v2 in visited:
                    continue
                heapq.heappush(minheap, [w1+w2, v2])
        return mindist if len(visited)==n else -1
