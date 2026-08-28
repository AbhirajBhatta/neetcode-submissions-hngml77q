class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1map, s2map = {}, {}
        for i in range(len(s1)):
            s1map[s1[i]] = 1 + s1map.get(s1[i], 0)
            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
        l=0
        if s1map==s2map:
                return True
        for r in range(len(s1), len(s2)):
            s2map[s2[r]] = 1 + s2map.get(s2[r], 0)
            if r-l+1 > len(s1):
                s2map[s2[l]]-=1
                if s2map[s2[l]]==0:
                    del s2map[s2[l]]
                l+=1
            if s1map==s2map:
                return True
            
            
        return False
            