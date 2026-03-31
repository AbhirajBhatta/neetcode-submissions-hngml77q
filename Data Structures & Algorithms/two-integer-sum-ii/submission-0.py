class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(numbers):
            needed = target - v
            if needed in seen:
                return [seen[needed], i+1]
            else:
                seen[v] = i+1
        return []