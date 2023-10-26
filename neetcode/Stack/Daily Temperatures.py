class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res=[0]*len(temperatures)
        stack =[] #append index and temperature
        for index,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                si,st=stack.pop()
                res[si]=index-si
            stack.append((index,t))
        return res
        
        
