class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t)>len(s)):
            return ""
        if s==t:
            return t
        window = {}
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        l = 0
        have, need = 0, len(countT)
        minLen = float("Infinity")
        resL, resR = 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    resL = l
                    resR = r
                if s[l] in countT:
                    window[s[l]]-=1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l+=1
        res = s[resL:resR+1]
        return res if minLen!=float("infinity") else ""
        
            
