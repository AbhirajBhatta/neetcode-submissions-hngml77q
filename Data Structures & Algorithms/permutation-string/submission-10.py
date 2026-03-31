class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return False
        counts1, counts2 = {}, {}
        for c in s1:
            counts1[c] = 1+ counts1.get(c, 0)
        
        l = 0
        for r in range(len(s2)):
            counts2[s2[r]] = 1+counts2.get(s2[r], 0)

            if (r-l+1)>len(s1):
                counts2[s2[l]] -= 1
                if(counts2[s2[l]]==0):
                    counts2.pop(s2[l])
                l+=1

            if (r-l+1)==len(s1) and counts1 == counts2:
                    return True
        return False

                
        

        