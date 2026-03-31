class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       char1 = {}
       char2 = {}
       for c in s:
        if c in char1:
            char1[c] += 1
        else:
            char1[c] = 1
       for c in t:
        if c in char2:
            char2[c] += 1
        else:
            char2[c] = 1
        
       if(char1 == char2):
        return True
       else:
        return False
        