from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        par_dic={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            if i in "]})":
                if not stack:
                    return False
                top=stack.pop()
                if par_dic[top] != i:
                    return False
                    break

        else:
            if not stack:
                return True 
            else:
                return False

