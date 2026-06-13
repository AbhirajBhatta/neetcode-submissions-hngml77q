class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            courseToPre[course].append(pre)
        def dfs(course):
            if course in visited:
                return False
            if not courseToPre[course]:
                return True
            visited.add(course)
            for need in courseToPre[course]:
                if not dfs(need):
                    return False
            visited.remove(course)
            courseToPre[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True