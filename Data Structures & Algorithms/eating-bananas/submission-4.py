class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        l, r = 1, maxRate
        res = maxRate
        while l<=r:
            k = (l+r)//2
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            if time > h:
                l = k+1
            else:
                res = min(res, k)
                r = k-1
        return res