class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        
        res = ["JFK"]
        def dfs(source):
            if len(res)==len(tickets)+1:
                return True
            if source not in adj:
                return False
            
            temp = adj[source]
            for i, nei in enumerate(temp):
                adj[source].pop(i)
                res.append(nei)
                if dfs(nei):
                    return True
                res.pop()
                adj[source].insert(i, nei)
            return False
        dfs("JFK")
        return res
        