class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        minheap = [[0, k]]
        visited = set()
        time = 0
        while minheap:
            w1, v1 = heapq.heappop(minheap)
            if v1 in visited:
                continue
            visited.add(v1)
            time = max(time, w1)
            
            for v2, w2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minheap, (w1+w2, v2))
        return time if len(visited)==n else -1