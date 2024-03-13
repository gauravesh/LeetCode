class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res=list()
        for i in range(len(candies)):
            what_to_append=True
            for j in range(len(candies)):
                if candies[i]+ extraCandies < candies[j]:
                    what_to_append=False
                    break
            res.append(what_to_append)
        return (res)
