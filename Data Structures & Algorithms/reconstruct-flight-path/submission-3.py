class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {i:[] for i, j in tickets}

        for i, j in tickets:
            adj[i].append(j)
        
        res = ["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = adj[src]
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v) : return True
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res