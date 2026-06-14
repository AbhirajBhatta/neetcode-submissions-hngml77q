class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodesMap = defaultdict(list)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for nei in nodesMap[node]:
                if nei==prev:
                    continue
                if dfs(nei, node):
                    return True
            visited.remove(node)
    
        for u, v in edges:
            nodesMap[u].append(v)
            nodesMap[v].append(u)
            if dfs(edges[0][0], -1):
                return [u, v]
        
