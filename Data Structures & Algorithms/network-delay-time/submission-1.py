class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)
        for u, v, w in times:
            nodes[u].append((v, w))
        visited = set()
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            t = max(t, w1)
            visited.add(v1)
            for v2, w2 in nodes[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, v2))
        return t if len(visited)==n else -1

        