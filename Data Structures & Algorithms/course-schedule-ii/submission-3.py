class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        res = [] 
        completed = set()
        def dfs(course):
            if course in completed:
                return False
            if course in cycle:
                return True
            
            cycle.add(course)
            for nei in adj[course]:
                if dfs(nei):
                    return True
            cycle.remove(course)
            completed.add(course)
            res.append(course)
            return False
        for course in range(numCourses):
            if dfs(course):
                return []
        return res
