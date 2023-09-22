class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = dict()

        # Count the frequency of each element in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort the unique elements by their frequencies in descending order
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # Return the top k frequent elements
        return sorted_elements[:k]
