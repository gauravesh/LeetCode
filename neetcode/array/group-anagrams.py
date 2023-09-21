class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dic=dict()
        for i in strs:
            sorted_word=''.join(sorted(i))
            if sorted_word not in anagram_dic:
                anagram_dic[sorted_word]=[i]
            else:
                anagram_dic[sorted_word].append(i)
        return list(anagram_dic.values())
        
