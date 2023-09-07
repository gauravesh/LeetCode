class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3) % 2 == 1:
            return (nums3[len(nums3)//2])
        elif len(nums3) % 2 == 0:
           mid1= nums3[len(nums3)//2]
           mid2 = nums3[len(nums3)//2 - 1]
           print(mid1)
           print(mid2)
           mid = ((mid1+mid2)/2.0)
           return(mid)


