class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for n,c in count.items():
            res[c].append(n)
        
        fin = []
        for i in range(len(res)-1, 0, -1):
            for n in res[i]:
                fin.append(n)
                if(len(fin)==k):
                    return fin