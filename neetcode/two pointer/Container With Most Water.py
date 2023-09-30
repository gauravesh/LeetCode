class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        L=0
        R=len(height)-1
        max_area_list=list()


        while(L<R):
            area = (R-L) * min (height[L],height[R])
            max_area_list.append(area)
            if height[L] < height [R]:
                L+=1
            else:
                R -=1
            
        return (max(max_area_list))


       
