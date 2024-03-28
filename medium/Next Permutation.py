class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        original_nums=nums.copy() #copying the original array 

        #getting numbers in sorted way
        sorted_nums=nums.copy()
        sorted_nums.sort()


        numbered_list=list()  #list for numbers from 0 to len(n)-1


        for i in range(len(nums)):
            numbered_list.append(i)

        def permutations(array):
            # base case if length is 2 return swap and original permutations
            if len(array)==2:
                res=list() # temp list that returns array
                res.append(array.copy()) #appending original permutation

                #simple swap operation

                temp=array[1]
                array[1]=array[0]
                array[0]=temp



                res.append(array.copy()) # copy the modified array

                return res # returned list[list[]]

            return_array=list() 

            for i in array: 
                temp_array=array.copy()
                temp_array.remove(i)
                for j in permutations(temp_array):
                    return_array+=[[i]+j]
            return return_array


        # list that stores all permutations of the index
        save_permutations=(permutations(numbered_list))

        #print(save_permutations)

        #variable to store the space 
        saver=list()

        #checking for the index that matches with nums
        for permutation in save_permutations:
            if originaL_nums[permutation[0]] == original_nums[0]:
                for check in range(len(nums)+1):
                    if i == len(nums):
                        saver=permutation
                        break
                    elif originaL_nums[permutation[check]] == original_nums[check]:

                        
                    


    

        
        
