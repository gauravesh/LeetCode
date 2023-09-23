class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = {}
        max_length = 0
        start = 0  # Starting index of the current substring

        for i in range(len(s)):
            if s[i] in dict_s and dict_s[s[i]] >= start:
                start = dict_s[s[i]] + 1

            dict_s[s[i]] = i  # Store the index of the character
            max_length = max(max_length, i - start + 1)

        return max_length
