class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rotate(nums):

            end=nums[-1]
            sample=list()
            for i in nums:
                sample.append(i)
            for i in range(len(nums)-1):
                nums[i+1]=sample[i]
            nums[0]=end
        for i in range(k):
            rotate(nums)
        print(nums)


        
