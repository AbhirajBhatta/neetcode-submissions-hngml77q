class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res+=1
        return res
            