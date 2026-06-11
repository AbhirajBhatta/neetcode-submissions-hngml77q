class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums:
            nums.add(n)
            new = 0
            while n>0:
                new += (n%10)**2
                n//=10
            n = new
            if n==1: return True
        return False