class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        
        for index_i, i in enumerate(height):
            for index_j, j in enumerate(height):
                if index_i < index_j:
                    # Calculate the width as the difference between indices
                    width = index_j - index_i
                    # Calculate the height as the minimum of the two heights
                    min_height = min(i, j)
                    # Calculate the area and update max_area if needed
                    area = width * min_height
                    max_area = max(max_area, area)
        
        return max_area
