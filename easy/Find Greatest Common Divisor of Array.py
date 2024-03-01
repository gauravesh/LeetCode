class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def Gcd(num1,num2):
            if num1 % num2 == 0:
                return num2
            elif num2 > num1 :
                return Gcd(num2,num1)
            else:
                return Gcd(num1%num2,num2)
        a=nums[0]
        b=nums[-1]
        res=Gcd(a,b)
        return res

        
