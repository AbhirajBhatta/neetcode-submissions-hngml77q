class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()

        adj = defaultdict(list)

        def dfs(node, prev):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                if dfs(nei, node):
                    return True
            visited.remove(node)
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            if dfs(edges[0][0], -1):
                return [ u, v]
        

        