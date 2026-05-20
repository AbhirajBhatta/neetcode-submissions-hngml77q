class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = None
        while top<=bottom:
            mid = (top+bottom)//2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                row = mid
                break
        if row is None: return False
        l, r = 0, len(matrix[row])-1
        while l<=r:
            mid = (l+r)//2

            if target < matrix[row][mid]:
                r = mid-1
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                return True
        return False
