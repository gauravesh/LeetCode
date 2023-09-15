import itertools

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input list
        
        all_list = list(itertools.combinations(nums, 3))
        final_list = []
        
        for combo in all_list:
            if sum(combo) == 0 and list(combo) not in final_list:
                final_list.append(list(combo))
        
        return final_list

