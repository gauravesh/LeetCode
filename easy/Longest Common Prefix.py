class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        number_of_strings = len(strs)
        print(number_of_strings)
        longest_prefix = ""

        if number_of_strings == 0:
            return longest_prefix

        shortest_string = min(strs, key=len)

        for index_i, char in enumerate(shortest_string):
            for other_string in strs:
                if other_string[index_i] != char:
                    return longest_prefix
            longest_prefix += char

        return longest_prefix

