class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        window = {}

        for c in s1:
            counts1[c] = 1+counts1.get(c, 0)
        l = 0
        k = len(s1)
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if r-l+1 > k:
                window[s2[l]] -= 1
                if window[s2[l]]==0: del window[s2[l]]
                l+=1
            if r-l+1 == k and window==counts1:
                return True
        return False
