class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #convert a list to set 
        #if length of set == lenght of list then false else true
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        return True
        
