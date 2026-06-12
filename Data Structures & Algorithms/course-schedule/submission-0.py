class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courseToNeed = {i:[] for i in range(numCourses)}
        for need, course in prerequisites:
            courseToNeed[course].append(need)
        
        def dfs(course):
            if course in visited:
                return False
            if not courseToNeed[course]:
                return True

            visited.add(course)
            for need in courseToNeed[course]:
                if not dfs(need):
                    return False
            visited.remove(course)
            courseToNeed[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            