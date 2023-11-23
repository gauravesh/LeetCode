class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        count=1
        for i in columnTitle[::-1]:
            res=res+(ord(i)-ord('A')+1)*count
            count*=26
        return (res)

        
