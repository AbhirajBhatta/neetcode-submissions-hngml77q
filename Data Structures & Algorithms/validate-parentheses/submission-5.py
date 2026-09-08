class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"]":"[", "}":"{", ")":"("}
        stack = []
        for p in s:
            if stack and p in mapping and stack[-1]==mapping[p]:
                stack.pop()
            else:
                stack.append(p)
        return len(stack)==0