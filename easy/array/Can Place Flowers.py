class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 1  and flowerbed[i+1] == 1:
                return False
            elif flowerbed[i] == 1 and flowerbed[i+1] == 0:
                continue
            elif flowerbed[i]==0 and flowerbed[i+1] == 1:
                continue
            else :
                flowerbed[i+1] = 1
                n=n-1
                continue
        print(flowerbed)
        print(n)
        if n != 0:
            return False
        return True
        
