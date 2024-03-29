from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        first=deque()
        second=deque()
        f=list()
        s=list()
        if root:
            first.append(root)
           
        #BFS

        while first:
            temp=list()
            for i in range(len(first)):
                node1=first.popleft()
                temp.append(node1.val)
                
                if node1.left:
                    first.append(node1.left)
                    
                    
                if node1.right:
                    first.append(node1.right)
                    
      
            f.append(temp)

        print(f)
        return f
