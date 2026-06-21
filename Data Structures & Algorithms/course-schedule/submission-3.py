class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for c, p in prerequisites:
            preMap[c].append(p)
        
        def dfs(course):
            if not preMap[course]:
                return True
            if course in visited:
                return False
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True