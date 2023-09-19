class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = {}
        for index_j,j in enumerate(nums):
            diff = target - j
            if diff in start:
                return [start[diff],index_j]
            start[j]=index_j
        return
