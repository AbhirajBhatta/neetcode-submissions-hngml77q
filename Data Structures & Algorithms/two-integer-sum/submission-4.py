class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, v in enumerate(nums):
            need = target - v
            if v in needs:
                return [needs[v], i]
            else:
                needs[need] = i