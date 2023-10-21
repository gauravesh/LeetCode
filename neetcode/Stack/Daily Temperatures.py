from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack=deque()
        res=[]
        for index_i in range(len(temperatures)):
            found=False
            for index_j in range(index_i+1,len(temperatures)):
                #print(index_i,index_j)
                if temperatures[index_i] < temperatures[index_j]:
                    res.append(index_j-index_i)
                    found=True
                    break
            if found == False:
                res.append(0)

        
        
        return res
