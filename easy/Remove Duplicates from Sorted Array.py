class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=0
        for i in range(1,len(nums)):
            if nums[sums] != nums[i]:
                sums +=1
                nums[sums] = nums[i]
        return sums + 1
        
