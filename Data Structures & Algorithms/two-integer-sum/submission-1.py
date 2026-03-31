class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            needed = target - v
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[v] = i
        return []
        
            