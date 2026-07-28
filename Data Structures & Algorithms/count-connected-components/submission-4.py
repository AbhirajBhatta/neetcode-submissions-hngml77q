class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        res = 0
        def dfs(node, prev):
            if node in visited:
                return 
            visited.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                if dfs(nei, node):
                    return 
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res+=1
        return res