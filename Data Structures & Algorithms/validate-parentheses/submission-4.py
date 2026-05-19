class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing = {"]": "[", "}":"{", ")":"("}

        for brac in s:
            if stack and brac in closing and stack[-1] == closing[brac]:
                stack.pop()
            else:
                stack.append(brac)
        return False if stack else True