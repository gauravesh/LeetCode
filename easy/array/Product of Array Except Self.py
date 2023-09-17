
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod=1
        zero=0
        for i in nums:
            if i == 0:
                zero += 1
                continue
            prod *= i 
        
        
        final_array=[]

        if zero >= 2:
            for i in nums:
                final_array.append(0)
        if zero  == 1:
            for i in nums:
                if i == 0:
                    final_array.append(prod)
                else:
                    final_array.append(0)
        if zero == 0:
            for i in nums:
                final_array.append(prod/i)
            
        return (final_array)
