class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1count, s2count = {}, {}
        for c in s1:
            s1count[c] = 1 + s1count.get(c, 0)
        
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)

            if r-l+1 > k:
                s2count[s2[l]] -= 1
                if s2count[s2[l]]==0:
                    s2count.pop(s2[l])
                l+=1
            if r-l+1 == k and s1count==s2count:
                return True
        return False