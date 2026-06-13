class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodesMap = {i:[] for i in range(n)}
        visited = set()
        for s, d in edges:
            nodesMap[s].append(d)
            nodesMap[d].append(s)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in nodesMap[node]:
                dfs(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count