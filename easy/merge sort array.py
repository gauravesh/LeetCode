class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x=[]
        for i in range(m):
            x.append(nums1[i])
        #print(x)
        y=[]
        for j in range(n):
            y.append(nums2[j])
        #print(y)
        list3=x+y
        list3.sort()
        print(list3)



