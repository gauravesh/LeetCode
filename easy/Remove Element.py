class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=len(nums)
        i=0
        j=len(nums)-1
        while i < j:
            if nums[i] == val:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j=j-1
                print(nums)
            else:
                i+=1
        res=0
        print(nums)
        for i in nums:
            if i != val:
                res+=1
        return res

                
        
