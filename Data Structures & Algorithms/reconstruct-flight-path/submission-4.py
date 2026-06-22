class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {i:[] for i, j in tickets}
        for u, v in tickets:
            adj[u].append(v)
        
        
        res = ["JFK"]
        def dfs(source):
            if len(res)==len(tickets)+1:
                return True
            if source not in adj:
                return False
            temp = adj[source]
            for i, v in enumerate(temp):
                adj[source].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[source].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res