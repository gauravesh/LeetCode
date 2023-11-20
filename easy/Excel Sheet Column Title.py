class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #print(ord('Z')-ord('A')+1)

        res=str()

        while columnNumber > 0 :
            columnNumber=columnNumber-1
            first=columnNumber%26
            res= chr(first+ord('A'))+res
            columnNumber=int(columnNumber/26)
        return res
