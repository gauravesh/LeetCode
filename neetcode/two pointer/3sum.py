import itertools

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        
        all_list = []
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    a=[nums[i],nums[j],nums[k]]
                    all_list.append(a)
                    j +=1
                    k -=1
                elif  (nums[i]+nums[j]+nums[k]) < 0:
                    j +=1
                else :
                    k-=1



        # Remove duplicates
        
        final_list = []
        for i in all_list:
            if sum(i) == 0 and list(i) not in final_list:
                final_list.append(list(i))
        return final_list
