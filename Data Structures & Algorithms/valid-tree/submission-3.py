class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {u:[] for u in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(s, prev):
            if s in visited:
                return False 
            visited.add(s)
            for nei in adj[s]:
                if nei==prev:
                    continue
                if not dfs(nei, s):
                    return False
            return True
        
        return dfs(0, -1) and len(visited)==n 
        
