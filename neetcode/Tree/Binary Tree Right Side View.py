# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        li=list()
        if not root:
            return []
            
        li.append(root.val)
        if root.right:
            li+=self.rightSideView(root.right)
        
        
        return li
