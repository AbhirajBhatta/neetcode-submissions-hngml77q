class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap = {}
        for integer in nums:
            if integer in mymap:
                mymap[integer] +=1
            else:
                mymap[integer]=1
        for integer in nums:
            if mymap[integer] > 1:
                return True
        else:
            return False