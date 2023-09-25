class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #remove all spaces        
        str_pal=str(s)
        s1=''.join(c for c in str_pal if c.isalnum())
        str_pal=s1.lower()



        #palindrome

        first_character = 0
        second_character=len(str_pal)-1
        if not str_pal:
            return True


        for temper in str_pal:
            if first_character == second_character or first_character > second_character:
                
                return True
            if str_pal[first_character] == str_pal[second_character] :
                
                first_character += 1
                second_character -= 1
                
            else:

                return False

        
