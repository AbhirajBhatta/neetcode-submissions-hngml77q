class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        minh = []
        count = {}
        for n in hand:
            if n not in count:
                heapq.heappush(minh, n)
            count[n] = 1+count.get(n, 0)
        while minh:
            minval = minh[0]

            for i in range(minval, minval+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minh[0]:
                        return False
                    heapq.heappop(minh)
        return True