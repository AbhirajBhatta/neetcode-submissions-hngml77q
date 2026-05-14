class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        window = {}
        for i in s1:
            counts1[i] = 1+counts1.get(i, 0)
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = 1+window.get(s2[r], 0)
            if r-l+1 > k:
                window[s2[l]] -= 1
                if window[s2[l]] == 0 : del window[s2[l]]
                l+=1
            if r-l+1 == k and window==counts1:
                return True
        return False