# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        x=root.right
        y=root.left
        root.left=x
        root.right=y
        

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
            
        
