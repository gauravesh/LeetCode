class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res=[]
        for index in range(len(haystack) - len(needle) + 1 ):
            if haystack[index] == needle[0]:
                j=0
                while (j < len(needle) and haystack[index + j] == needle[j]):
                    j=j+1
                if j == len(needle):
                    res.append(index)
        if not res:
            return -1
        x = (min(res))
        return x
