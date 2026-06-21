class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finished, cycle = set(), set()

        adj = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)   

        res = [] 
        def dfs(course):
            if course in cycle:
                return False
            if course in finished:
                return True
            
            cycle.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            finished.add(course)
            res.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

    