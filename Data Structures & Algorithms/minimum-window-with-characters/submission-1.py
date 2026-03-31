class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        l = 0
        countT, win = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            c = s[r]
            win[c] = win.get(c, 0) + 1
            if c in countT and win[c]==countT[c]:
                have += 1 
            while have==need:
                if (r-l+1)<resLen:
                    res = [l, r]
                    resLen = r-l+1
                win[s[l]] -= 1
                if s[l] in countT and win[s[l]]<countT[s[l]]:
                    have -= 1
                l+=1
        
        l, r = res
        resLen = r-l+1
        return s[l:r+1] if resLen != float("infinity") else ""