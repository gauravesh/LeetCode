class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s,f=0,0
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f:
                break
        se=0
        while True:
            s=nums[s]
            se=nums[se]
            if s==se:
                return s
