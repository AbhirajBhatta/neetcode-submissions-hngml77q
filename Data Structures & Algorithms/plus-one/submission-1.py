class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        s = (1+ digits[i])%10
        carry = (1+ digits[i])//10
        digits[i] = s
        i-=1
        while i>=0 and carry:
            s = (1+ digits[i])%10
            carry = (1+ digits[i])//10
            digits[i]= s
            i-=1
        if carry:
            digits.insert(0, 1)
        return digits