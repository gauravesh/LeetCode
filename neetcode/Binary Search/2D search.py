class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col_size=len(matrix)
        l=0
        r=len(matrix)-1
        mid=l+r//2
        store_list=[]
        if target<matrix[0][0] or target > matrix[-1][0]:
            return False
        while abs(r-l) != 1 or r-l != 0:
            if target <matrix[mid][0]:
                r=mid-1
            if target > matrix[mid][0]:
                
            
