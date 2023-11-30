class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=dict()
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        print(dic)
        length=0
        found=0
        for index in dic:
            lengther=dic[index]
           # print(index,end=':')
            while int(lengther//2) != 0:
                #print(lengther)

                lengther=lengther-2
               
                length+=1
        for i in dic:
            if dic[i] % 2==1:
                found=1
                break
        return (length*2)+found
            
