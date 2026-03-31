class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(nums)
        seqLen = 1
        maxlen = 1
        if(len(n)==0):
            return 0
        current = n[0]
        for i in range(1, len(n)):
            if(n[i]-current==1):
                current = n[i]
                seqLen+=1
                if(maxlen<seqLen):
                    maxlen = seqLen
            elif(current-n[i]==0):
                continue
            else:
                current=n[i]
                seqLen = 1
        return maxlen
