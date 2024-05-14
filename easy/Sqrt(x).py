import math

class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        res=0
        while low <= x :
            x=x-low
            low=low+2
            res+=1
        return res

        
