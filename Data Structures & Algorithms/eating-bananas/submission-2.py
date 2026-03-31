class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k  
        while l<=r:
            m = (l+r)//2
            time = 0
            for p in piles:
                time += math.ceil(p/m)
            if time <= h:
                k = min(k, m)
                r = m-1
            else :
                l = m+1
        
        return k
