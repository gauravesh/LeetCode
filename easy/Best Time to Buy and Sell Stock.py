class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        has1=dict()
        has2=dict()
        for i in ransomNote:
            if i in has1:
                has1[i]+=1
            else:
                has1[i]=1
        for j in magazine:
            if j in has2:
                has2[j]+=1
            else:
                has2[j]=1
        
        
        for i in has1:
            print('this is i',i)
            if i in has2:
                print('here',i)
                if has1[i] > has2[i]:
                    has1[i]=has1[i]-has2[i]
                    has2[i]=0
                elif has1[i] < has2[i]:
                    has2[i]= has2[i]-has1[i]
                    has1[i]=0
                else:
                    has1[i]=0
                    has2[i]=0
        for i in has1:
            if has1[i] != 0:
                return False
        return True        

