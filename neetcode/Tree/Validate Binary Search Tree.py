
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def parent(r,low,high):
            if not r:
                return True
            if (low is not None and r.val <= low) or (high is not None and r.val >=high):
                return False
            return parent(r.left,low,r.val) and parent(r.right,r.val,high)
        return parent(root,float('-inf'),float('inf'))
