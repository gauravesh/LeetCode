class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        sample=piles
        sample.sort()
        for i in range(h-len(piles)):
            
            a=sample[-1]
            if a%2==0:
                x=y=(a//2)

            if a%2==1:
                a=a//2
                x,y=a,a+1

            sample=sample[:-1]
            
            sample.append(x)
            sample.append(y)
            sample.sort()
            print(sample)
        sample.sort()
        return sample[-1]
