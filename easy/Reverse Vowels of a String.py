from collections import deque

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=str()
        vovel_deque=deque()
        for i in s:
            if i == 'a' or  i == 'e' or  i == 'i' or  i == 'o' or  i == 'u' or i == 'A' or  i == 'E' or  i == 'I' or  i == 'O' or  i == 'U':
                vovel_deque.append(i)
        for i in s:
            if i == 'a' or  i == 'e' or  i == 'i' or  i == 'o' or  i == 'u' or i == 'A' or  i == 'E' or  i == 'I' or  i == 'O' or  i == 'U':
                res+=vovel_deque.pop()
            else:
                res+=i
        return res
             
