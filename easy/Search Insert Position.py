class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        middle=l+r
        while l<=r:
            middle=(l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l=middle+1
            else:
                r=middle-1
        return l
