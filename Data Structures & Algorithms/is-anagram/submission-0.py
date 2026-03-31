class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap1 ={}
        charMap2 = {}
        for char1 in s:
            if char1 in charMap1:
                charMap1[char1] +=1
            else:
                charMap1[char1] = 1
        for char2 in t:
            if char2 in charMap2:
                charMap2[char2] +=1
            else:
                charMap2[char2] = 1

        if charMap1 == charMap2:
            return True
        else: 
            return False
        