class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s :
            return True
        ls=0
        rs=len(s)
        lt=0
        rt=len(t)
        while(lt < rt):

            print('lt,rt',lt,rt,'ls,rs',ls,rs)
            if s[ls] == t[lt]:
                ls+=1
                if ls == rs :
                    return True

            lt+=1
        print('here')
        return False
                
                

