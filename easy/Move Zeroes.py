class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l -= 1  
            else:
                i += 1
