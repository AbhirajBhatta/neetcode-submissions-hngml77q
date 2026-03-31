class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        bucket = [[] for i in range(len(nums)+1)]

        for i in nums:
            countmap[i] = 1 + countmap.get(i, 0)
        for n, c in countmap.items():
            bucket[c].append(n)

        result = []

        for i in range(len(bucket)-1, 0, -1):
            for b in bucket[i]:
                result.append(b)
                if(len(result)==k):
                    return result
        
        
            
            
        