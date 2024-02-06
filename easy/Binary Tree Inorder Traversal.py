# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=list()
        if root == None:
            return
        if root.left:
            li += self.inorderTraversal(root.left)
        
        li.append(root.val)
        if root.right:
            li+= self.inorderTraversal(root.right)
        return li
