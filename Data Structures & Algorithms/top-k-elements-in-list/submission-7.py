class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for bucket in range(len(nums), -1, -1):
            for n in freq[bucket]:
                res.append(n)
            if len(res)==k:
                return res
        