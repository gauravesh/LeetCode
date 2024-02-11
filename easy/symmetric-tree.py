# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def traverse(node):
            li=list()
            if node.left:
                li += traverse(node.left)
            li.append(node.val)
            if node.right:
                li += traverse(node.right)
            return li
        values_right= traverse(root.right)
        values_left= traverse(root.left)
        print(values_right)
        values_left.reverse()
        print(values_left)
        if values_left == values_right:
            return True
        return False
        
