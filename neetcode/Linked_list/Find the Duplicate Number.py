class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has=set()
        for i in nums:
            if i in has:
                return i 
            has.add(i)

        
        
            


        
        
