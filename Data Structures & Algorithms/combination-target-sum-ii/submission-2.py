class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        current = []

        def dfs(i):
            if sum(current)==target:
                res.append(current.copy())
                return
            if sum(current)>target or i==len(candidates):
                return
            
            current.append(candidates[i])
            dfs(i+1)
            current.pop()

            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res
