class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                if dfs(nei, node):
                    return True
            
            return False
        if dfs(0, -1):
            return False
        return True if len(visited)==n else False
