lass Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[]
        mult=1
        for i in nums:
            mult=mult*i
            prefix.append(mult)

        
        del prefix[len(prefix)-1]
        prefix = [1]+prefix
        
        
        postfix=[]
        r_nums=nums
        r_nums.reverse()
        mult=1
        
        for i in r_nums:
            mult*=i
            postfix.append(mult)
       
        postfix.reverse()
        del postfix[0]
        postfix.append(1)
        



        final = []
        for i in range(len(postfix)):
            final.append(postfix[i]*prefix[i])
        return (final)

        #for i in range(len(r_nums)):
            
        
