class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        ps=[]
        for i in range(len(position)):
            ps.append((position[i],speed[i]))
        ps.sort(reverse=True)

        stack=[]
        for p,s in ps:
            time=float((target-p))/s
            stack.append(time)
            if len(stack) >1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
