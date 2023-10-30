class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l=0
        r=len(matrix)-1
        mid=(l+r)//2


        if target<matrix[0][0] or target > matrix[-1][-1]:
            return False
        while l<=r:
            if target == matrix[mid][0]:
                return True
            if target <matrix[mid][0]:
                r=mid-1
            if target > matrix[mid][0]:
                l=mid+1
            mid=(r+l)//2

            
        new=matrix[r]

        l=0
        r=len(new)-1
        mid=(l+r)//2
        while l<=r:
            if target==new[mid]:
                return True
            if target < new[mid]:
                r=mid-1
            if target > new[mid]:
                l= mid+1
            mid=(l+r)//2
        return False
        

        

            
