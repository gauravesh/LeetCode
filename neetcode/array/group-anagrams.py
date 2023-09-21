class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #we can find anagram 1 by 1
        check_set = set()
        for i in strs:
            sorted_str = ''.join(sorted(i))
            check_set.add(sorted_str)
         
        final_arr=[]
        for i in check_set:
            i_list=[]
            for j in strs:

                copy_j=''.join(sorted(j))

               # print("real::",j,"copy::",copy_j,"i::",i)
                if copy_j == i:
                    i_list.append(str(j))
            final_arr.append(i_list)
        return (final_arr)
