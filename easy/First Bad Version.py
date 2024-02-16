# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        i=0
        ajax=isBadVersion(i)
        print(ajax)

        '''
        while isBadVersion(i) != True and i != n:
            i+=1
            print("ee")
        return i

        '''

        l=0
        r=n
        while l<r:
            m=l+(r-l)//2
            if isBadVersion(m):
                right = mid
            else:
                left=m+1
        return l

        
