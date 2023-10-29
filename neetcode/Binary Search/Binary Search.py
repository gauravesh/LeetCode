class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) ==1:
            if nums[0]==target:
                return 0
            return -1

        left=0
        right=len(nums)-1
        mid=(left+right)//2
        
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                left= mid+1
            if nums[mid] > target:
                right=mid-1
            mid=(left+right)//2
        return -1


        
