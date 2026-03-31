class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqList = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1+count.get(i, 0)
        for n, c in count.items():
            freqList[c].append(n)
        
        res = []
        for i in range(len(freqList)-1, 0, -1):
            for n in freqList[i]:
                res.append(n)
                if len(res)==k:
                    return res
        