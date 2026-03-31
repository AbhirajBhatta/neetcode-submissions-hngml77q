class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        frequency = [[] for i in range(len(nums)+1)]
        for num, c in count.items():
            frequency[c].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res)==k:
                    return res