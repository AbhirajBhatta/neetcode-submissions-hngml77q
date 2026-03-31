class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return False
        countS1 = {}
        countS2 = {}
        for c in s1:
            countS1[c] = 1+countS1.get(c, 0)
        k = len(s1)
        for i in range(len(s2)-k+1):
            for j in range(i, i+k):
                countS2[s2[j]] = 1+countS2.get(s2[j], 0)
            if countS1==countS2:
                return True
            countS2.clear()
        return False
                
        

        