class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodesMap = defaultdict(list)

        for u, v, w in times:
            nodesMap[u].append((v, w))
        
        visited = set()
        minheap = [(0, k)]
        t = 0
        while minheap:
            w1, v1 = heapq.heappop(minheap)
            if v1 in visited:
                continue
            visited.add(v1)
            t = max(t, w1)
            for v2, w2 in nodesMap[v1]:
                if v2 not in visited:
                    heapq.heappush(minheap, (w1+w2, v2))
        return t if len(visited)==n else -1
