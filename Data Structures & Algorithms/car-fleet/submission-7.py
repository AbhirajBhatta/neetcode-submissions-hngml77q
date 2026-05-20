class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, speed in sorted(zip(position, speed), reverse=True):
            time = (target - pos)/speed
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)
