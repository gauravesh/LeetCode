import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        to_list=list()
        neg=False
        if x<0:
            neg=True
        x=abs(x)



        while (x != 0):
            a=x%10
            to_list.append(a)
            x=x//10
        res=int()
        for i in to_list:
            res=i+res*10
        #print(pow(3,2))
        

        if neg==True:
            res=-res

        if abs(res) > int(pow(2,31)-1):
            return 0
        return res

        

        
        
