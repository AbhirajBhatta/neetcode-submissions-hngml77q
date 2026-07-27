class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u, v in prerequisites:
            adj[u].append(v)
        visited = set()
        def dfs(course):
            if course in visited:
                return True
            visited.add(course)

            for nei in adj[course]:
                if dfs(nei):
                    return True
            visited.remove(course)
            return False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True