class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed), reverse = True):
            time = (target - p)/s
            if not stack:
                stack.append(time)
            if stack and stack[-1] < time:
                stack.append(time)
        return len(stack)