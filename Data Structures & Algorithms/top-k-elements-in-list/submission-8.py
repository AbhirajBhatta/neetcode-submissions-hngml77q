class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]

        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n, c in count.items():
            buckets[c].append(n)
        res = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res

