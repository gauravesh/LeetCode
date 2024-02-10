class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=str()
        if len(word1 )>=len( word2):
            res=0
            for i in range(len(word2)):
                res=i
                final+=word1[i]
                final+=word2[i]
            final+=word1[res+1:len(word1)]
        if len(word2) > len(word1):
            res=0
            for i in range(len(word1)):
                res=i
                final+=word1[i]
                final+=word2[i]
            final+=word2[res+1:len(word2)]
        return final

        
