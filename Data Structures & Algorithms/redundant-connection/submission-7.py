class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adj = defaultdict(list)
        def cycle(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if prev==nei:
                    continue
                if cycle(nei, node):
                    return True
            visited.remove(node)
            return False
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if cycle(edges[0][0], 0):
                return [u, v]
