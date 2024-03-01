class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res=''
        def Gcd(n1,n2):
            if n1 % n2 == 0:
                return n2
            elif n2>n1 :
                return Gcd(n2,n1)
            else:
                return Gcd(n1%n2,n2)
        if str1+str2 != str2+str1:
            return res
        
        l1=len(str1)
        l2=len(str2)
        g=Gcd(l1,l2)
        if str1 > str2:
            return str2[:g]
        else:
            return str1[:g]
        
        
        
