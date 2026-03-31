class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        l = 0
        countT, window = {}, {}
        minLen = float("infinity")
        minl, minr = 0, 0
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = 1+window.get(c, 0)
            if c in countT and window[c]==countT[c]:
                have+=1

            while have == need:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    minl = l
                    minr = r

                
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l+=1
        res = s[minl:minr+1]
        return res if minLen != float("infinity") else ""