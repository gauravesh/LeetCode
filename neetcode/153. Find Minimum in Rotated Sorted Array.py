class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return min(nums)
        l,r=0,len(nums)-1
        mid=(l+r)//2
        target=nums[mid]
        while l<r:
            if nums[l]>nums[r]:
                l=mid+1
            elif nums[l]<nums[r]:
                r=mid -1

            mid=(r+l)//2
            target=min(target,nums[mid])

            if nums[l]==nums[r]:
                return target
        




        
