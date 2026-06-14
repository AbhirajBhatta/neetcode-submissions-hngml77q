class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        nodesMap = {i:[] for i in range(n)}
        for v,u in edges:
            nodesMap[v].append(u)
            nodesMap[u].append(v)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in nodesMap[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res