from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self_worth=0
        q=deque([(root,self_worth)])

        left=0
        right=0

        
        while q:
            for i in range(len(q)):
                node,value=q.popleft()

                if node.left:
                    left=min(left,value-1)
                    q.append((node.left,value-1))
                if node.right:
                    right=max(right,value+1)
                    q.append((node.right,value+1))
        return abs(right-left)

        
