class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total//2

        if len(a)>len(b):
            a,b = b,a
        l, r = 0, len(a)-1

        while True:
            i = (l+r)//2
            j = half - i - 2

            al = a[i] if i>=0 else float("-infinity")
            ar = a[i+1] if i+1 < len(a) else float("infinity")
            bl = b[j] if j>=0 else float("-infinity")
            br = b[j+1] if j+1<len(b) else float("infinity")

            if al<=br and bl<=ar:
                if total%2:
                    return min(ar, br)
                else:
                    return (min(ar, br)+max(al, bl))/2
            elif al>br:
                r = i-1
            else:
                l = i+1
        