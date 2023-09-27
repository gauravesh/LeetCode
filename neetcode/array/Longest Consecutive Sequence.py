class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        a=nums
        a.sort()
        max_element=0
        final_list=list()
        for index_i,i in enumerate(a):
            if index_i <len(a)-1 and a[index_i+1]-a[index_i] == 0:
                continue
            
            
            elif index_i <len(a)-1 and a[index_i+1]-a[index_i] == 1  :
                max_element +=1
            
            else:
                final_list.append(max_element)
                max_element=0
        return(max(final_list)+1)
