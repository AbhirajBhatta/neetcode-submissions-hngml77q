class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)

        l, r = 1, rate
        while l<=r:
            time = 0
            mid = (l+r)//2

            for p in piles:
                time += math.ceil(p/mid)
            
            if time > h:
                l = mid+1
            else:
                rate = min(rate, mid)
                r = mid-1
        return rate