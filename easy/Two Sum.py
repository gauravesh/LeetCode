class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #nums=[2,7,11,15]
        #target=9

        for index_i,i in enumerate(nums):
            for index_j,j in enumerate(nums[index_i+1:]):
                if(i+j)==target:
                    #print("indices are",index_i,(index_i+1+index_j))
                    return_arr = [index_i,index_i+1+index_j]
                    return return_arr
                
