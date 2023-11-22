class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) is( 0 or 1 ):
            return 0
    
        max_val=0
        mn=0
        mx=1
        value_list=list()

        while (mx != len(prices)):
            if (prices[mx] < prices[mn]):
                mn=mx
            else:
                value_list.append(prices[mx]-prices[mn])
                mx+=1
        return max(value_list)
        

        
