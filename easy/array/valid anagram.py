class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #check which is large and swap 
        # t should always be less than s
        if len(t) != len(s):
            return False
        s_list = list(s)
        t_list = list(t)
            
        for ion in s_list:
            if ion not in t_list:
                return False
            t_list.remove(ion)
        return True
        
