class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_list=[]
        max_val=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                value=prices[j]-prices[i]
                if value >= max_val:
                    max_val=value
        return max_val

