class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        start = 0
        end = length - 1
        
        while start<end:
            while start<end and not (s[start].isalnum()):
                start +=1
            while start<end and not (s[end].isalnum()):
                end -=1

            if s[start].lower()!=s[end].lower() :
                return False
            start += 1
            end -= 1
        return True
            