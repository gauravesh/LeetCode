class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # Define the search range for Koko's eating speed
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if self.canFinish(piles, mid, h):
                # If it's possible to finish in mid speed, try lower speeds
                r = mid
            else:
                # Otherwise, try higher speeds
                l = mid + 1

        return l

    def canFinish(self, piles, speed, h):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h
