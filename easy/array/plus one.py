class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        convert_to_int=0
        for i,digit in enumerate(digits):
            convert_to_int += digit*(pow(10,len(digits)-i-1))
        convert_to_int=(int(convert_to_int))+1
        convert_to_string=str(convert_to_int)
        print(convert_to_int)

        res=list()


        for char in (convert_to_string):
            res.append(int(char))
        return (res)
