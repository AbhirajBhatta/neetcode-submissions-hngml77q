class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {i:[] for i, j in tickets}

        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = adj[src]
            for i, dest in enumerate(temp):
                adj[src].pop(i)
                res.append(dest)
                if dfs(dest): return True
                adj[src].insert(i, dest)
                res.pop()
            return False
        dfs("JFK")
        return res
                
