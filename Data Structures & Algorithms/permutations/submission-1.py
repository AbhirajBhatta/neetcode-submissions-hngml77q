class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return [[]]
        
        perm = self.permute(nums[1:])

        for p in perm:
            for i in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy)
        return res
    


            