class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        combination = []
        def dfs(i):
            if sum(combination)==target:
                res.append(combination.copy())
                return
            if sum(combination) > target or i==len(candidates):
                return
            
            
            combination.append(candidates[i])
            dfs(i+1)
            combination.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res