class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        mix=list(map(str,s.split()))
        
        res=' '.join(mix[::-1])
        return res
        
