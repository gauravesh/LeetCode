class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=list(map(str,s.split()))
        return len(st[-1])
