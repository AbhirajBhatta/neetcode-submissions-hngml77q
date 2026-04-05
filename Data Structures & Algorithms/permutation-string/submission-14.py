class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts1 = {}
        window = {}
        k=0
        for c in s1:
            counts1[c] = 1+counts1.get(c, 0)
            k+=1
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = 1+window.get(s2[r], 0)
            if r-l+1 > k:
                window[s2[l]] -= 1
                if window[s2[l]]==0:
                    window.pop(s2[l])
                l+=1
            if r-l+1 == k and counts1==window:
                return True
            
        return False
            
            
