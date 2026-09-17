class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target-pos)/spd
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)