class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {i:[] for i, v in tickets}
        for i, v in tickets:
            adj[i].append(v)

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
                res.pop()
                adj[source].insert(i, v)
            return False
        dfs("JFK")
        return res