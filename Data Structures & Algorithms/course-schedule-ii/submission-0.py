class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for course, need in prerequisites:
            preMap[course].append(need)
        visited = set()
        cycles = set()
        res = []

        def dfs(node):
            if node in visited:
                return True
            if node in cycles:
                return False
            
            cycles.add(node)
            for n in preMap[node]:
                if not dfs(n):
                    return False
            cycles.remove(node)
            visited.add(node)
            res.append(node)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

        
        