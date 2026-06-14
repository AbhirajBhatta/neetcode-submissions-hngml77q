class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        completed, InAcycle = set(), set()
        res = []
        for c, p in prerequisites:
            preMap[c].append(p)
        
        def dfs(course):
            if course in completed:
                return True
            if course in InAcycle:
                return False
            
            InAcycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            InAcycle.remove(course)
            completed.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
            
