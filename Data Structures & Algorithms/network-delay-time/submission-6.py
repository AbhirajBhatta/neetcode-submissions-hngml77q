class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}

        for u, v, w in times:
            adj[u].append([w, v])

        minH = [[0, k]]
        visited = set()
        time = 0

        while minH:
            w1, v1 = heapq.heappop(minH)
            if v1 in visited:
                continue
            visited.add(v1)
            time = max(time, w1)
            for w2, v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minH, [w1+w2, v2])
        return time if len(visited)==n else -1
                    

