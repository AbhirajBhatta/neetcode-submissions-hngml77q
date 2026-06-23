class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((w, v))

        minH = [[0, src, 0]]
        while minH:
            cost, node, stops = heapq.heappop(minH)
            if node==dst:
                return cost
            if stops > k:
                continue
            for neiCost, nei in adj[node]:
                heapq.heappush(minH, (neiCost + cost, nei, stops+1))
        return -1