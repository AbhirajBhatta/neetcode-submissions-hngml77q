class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur):

            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur)
            cur.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]: i+=1
            dfs(i+1, cur)
        dfs(0, [])
        return res