class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        sums=0
        for index, i in enumerate(s_list):
    
            if i == 'I' and index + 1 < len(s_list) and s_list[index + 1] == 'V':
                sums += 4
            elif i == 'I' and index + 1 < len(s_list) and s_list[index + 1] == 'X':
                sums += 9
            elif i == 'X' and index + 1 < len(s_list) and s_list[index + 1] == 'L':
                sums += 40
            elif i == 'X' and index + 1 < len(s_list) and s_list[index + 1] == 'C':
                sums += 90
            elif i == 'C' and index + 1 < len(s_list) and s_list[index + 1] == 'D':
                sums += 400
            elif i == 'C' and index + 1 < len(s_list) and s_list[index + 1] == 'M':
                sums += 900
            elif i == 'M':
                if index > 0 and s_list[index - 1] == 'C':
                    continue
                sums += 1000
            elif i == 'D':
                if index > 0 and s_list[index - 1] == 'C':
                    continue
                sums += 500
            elif i == 'C':
                if index > 0 and s_list[index - 1] == 'X':
                    continue
                sums += 100
            elif i == 'L':
                if index > 0 and s_list[index - 1] == 'X':
                    continue
                sums += 50
            elif i == 'X':
                if index > 0 and s_list[index - 1] == 'I':
                    continue
                sums += 10
            elif i == 'V':
                if index > 0 and s_list[index - 1] == 'I':
                    continue
                sums += 5
            elif i == 'I':
                sums += 1
                
        return (sums)
