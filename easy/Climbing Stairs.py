class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first=0
        second=1
        total=0
        for _ in range(n):

            total=first+second
            first=second
            second=total 
        return total
            
