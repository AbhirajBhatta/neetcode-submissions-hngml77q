class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry = 0
        s = (digits[i] + 1)%10
        carry = (digits[i] + 1)//10
        digits[i] = s
        i-=1
        while carry>0 and i>=0:
            s = (digits[i] + 1)%10
            carry = (digits[i] + 1)//10
            digits[i] = s
            i-=1
        if carry:
            digits.insert(0, 1)
        return digits