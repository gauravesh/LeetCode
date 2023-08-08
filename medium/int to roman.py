class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        decimal_to_roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        character_list = []
        
        sorted_keys = sorted(decimal_to_roman.keys(), reverse=True)
        
        for key in sorted_keys:
            while num >= key:
                character_list.append(decimal_to_roman[key])
                num -= key
        
        return ''.join(character_list)


      

