class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1
        col = None
        while top<=bottom:
            mid = (top+bottom)//2
            if target>matrix[mid][-1]:
                top = mid +1
            elif target<matrix[mid][0]:
                bottom = mid-1
            else:
                col = mid
                break
        if col ==None:
            return False
        while l<=r:
            mid = (l+r)//2
            if target>matrix[col][mid]:
                l = mid+1
            elif target<matrix[col][mid]:
                r = mid-1
            else:
                return True
        return False