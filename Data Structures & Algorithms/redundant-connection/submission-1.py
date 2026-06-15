class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodesMap = defaultdict(list)
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for n in nodesMap[node]:
                if n==prev: continue
                if dfs(n, node):
                    return True
            visited.remove(node)
        
        for u, v in edges:
            nodesMap[u].append(v)
            nodesMap[v].append(u)
            if dfs(edges[0][0], -1):
                return [u, v]